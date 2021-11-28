<link rel="stylesheet" href="/css/styles.css">
<div id="ticket_form">
<h3 class="text-center">Ticket Details</h3>
    <table class=table>
         <tr class="thead-dark">
                <th scope="col">ID</th>
                <th scope="col">Subject</th>
                <th scope="col">Description</th>
                <th scope="col">Status</th>
                <th scope="col">Date</th>
            </tr>
            <tr>
                <td> {{feedback['ticket']['id']}}</td>
                <td>{{feedback['ticket']['subject']}}</td>
                <td> {{feedback['ticket']["description"]}}</td>
                <td>{{feedback['ticket']["status"]}}</td>
                <td>{{feedback['ticket']["created_at"]}}</td>
            </tr>
    </table>
    <a class="btn btn-dark" href="/tickets"> Back     </a>
</div>