"""
Created on Nov 25 2021

ZendeskChallenge

@author: João Paulo Carvalho
"""

#import libraries
from bottle import route, template, run, request, static_file, error
import requests

#authentication
user = 'jpcscarvalho@gmail.com'+'/token'
token = 'ZQapSQz8rlzBYmLo2ZdyHrQodocfD6VRXuklQtiM'
    
#Check if the API is available and the URL is valid
@error(404)
def error404(error):
    return 'Either you are requesting an invalid URL or the resource in question does not exist'

#Check for a few more possible general errors and display a friendly message
def errors(response):
    if response.status_code == 401:
        status = 'Could not authenticate you. Check your email address or register.'
    elif response.status_code == 400:
        status = 'Your request is invalid and/or not formed properly. You need to reformulate your request.'
    elif response.status_code == 403:
        status = 'We understand your request, but are refusing to fulfill it.'
    elif response.status_code == 500:
        status = 'We did something wrong. We will be notified and we will look into it.'
    else:
        status = 'Problem with the request. Status ' + str(response.status_code)
    return status

#First route called, it returns a template with the first 25 tickets in the list
@route('/tickets')
def tickets():
    url = 'https://zccjoaopaulo.zendesk.com/api/v2/tickets.json?per_page=25'
    #The variable 'response' receives information from the API
    response = requests.get(url,auth=(user,token))
    #Checks if everything is good before returning the template 'list_form' with the tickets
    if response.status_code != 200:
        #If a problem is found, returns template 'errorMessage' with an error description
        return template('errorMessage', feedback=errors(response))
    return template('list_form', feedback=response.json())

#This route is called when changing pages by number. 
#The page number comes as a parameter from the template, and it is concateneted to the URL
@route('/more_tickets_byNumber/<id:int>')
def moreTicketsByNumber(id):
    url = 'https://zccjoaopaulo.zendesk.com/api/v2/tickets.json?page='+str(id)+'&per_page=25'
    response = requests.get(url,auth=(user,token))
    if response.status_code != 200:
        return template('errorMessage', feedback=errors(response))
    return template('list_form', feedback=response.json())

#This route is called when changing pages by pressing 'Next' or 'Previuos'
#Each JSON page provides a URL for next and previous pages. 
#The variable 'url' receives this information and checks if it is equal to 'None' 
    #before sending the URL to a get request
@route('/more_tickets')
def moreTickets():
    url = request.query.url
    if url=='None':
        status = 'Invalid Page'
        return template('errorMessage', feedback=status)
    url = url+'&per_page=25'
    response = requests.get(url,auth=(user,token))
    if response.status_code != 200:
        return template('errorMessage', feedback=errors(response))
    return template('list_form', feedback=response.json())

#This route receives a ticket ID as parameter and diplay a few more information about this ticket
#If response.status_code == 200 (OK!). It returns a template called 'ticket_form'
@route('/detalhe/<id:int>')
def details(id):
    url='https://zccjoaopaulo.zendesk.com/api/v2/tickets/'+str(id)+'.json'
    response = requests.get(url, auth=(user, token))
    if response.status_code != 200:
        return template('errorMessage', feedback=errors(response))
    return template('ticket_form',feedback=response.json())

#This route allows access to the CSS file
@route('/css/<filename>')
def send_css(filename):
    return static_file(filename, root='static/css')

#Run application at port '8080'
run(host='localhost', port='8080', debug='true')