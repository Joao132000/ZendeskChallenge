from bottle import route, template, run, request, static_file
import requests

user = 'jpcscarvalho@gmail.com'+'/token'
token = 'ZQapSQz8rlzBYmLo2ZdyHrQodocfD6VRXuklQtiM'
    
def error(response):
    if response.status_code == 401:
        status = 'Could not authenticate you. Check your email address or register.'
    elif response.status_code == 400:
        status = 'Your request is invalid and/or not formed properly. You need to reformulate your request.'
    elif response.status_code == 403:
        status = 'We understand your request, but are refusing to fulfill it.'
    elif response.status_code == 404:
        status = 'Either you are requesting an invalid URI or the resource in question does not exist'
    elif response.status_code == 500:
        status = 'We did something wrong. We will be notified and we will look into it.'
    else:
        status = 'Problem with the request. Status ' + str(response.status_code)
    return status

@route('/tickets')
def tickets():
    url = 'https://zccjoaopaulo.zendesk.com/api/v2/tickets.json?per_page=25'
    response = requests.get(url,auth=(user,token))
    if response.status_code != 200:
        return template('errorMessage', feedback=error(response))
    return template('list_form', feedback=response.json())

@route('/more_tickets_byNumber/<id:int>')
def moreTicketsByNumber(id):
    url = 'https://zccjoaopaulo.zendesk.com/api/v2/tickets.json?page='+str(id)+'&per_page=25'
    response = requests.get(url,auth=(user,token))
    if response.status_code != 200:
        return template('errorMessage', feedback=error(response))
    return template('list_form', feedback=response.json())

@route('/more_tickets')
def moreTickets():
    url = request.query.url
    if url=='None':
        status = 'Invalid Page'
        return template('errorMessage', feedback=status)
    url = url+'&per_page=25'
    response = requests.get(url,auth=(user,token))
    if response.status_code != 200:
        return template('errorMessage', feedback=error(response))
    return template('list_form', feedback=response.json())

@route('/detalhe/<id:int>')
def details(id):
    url='https://zccjoaopaulo.zendesk.com/api/v2/tickets/'+str(id)+'.json'
    response = requests.get(url, auth=(user, token))
    if response.status_code != 200:
        return template('errorMessage', feedback=error(response))
    return template('ticket_form',feedback=response.json())

@route('/css/<filename>')
def send_css(filename):
    return static_file(filename, root='static/css')

run(host='localhost', port='8080', debug='true')