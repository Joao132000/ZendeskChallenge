<link rel="stylesheet" href="/css/styles.css">
<div id="list_form">
    <form>
        <h3>ZendeskChallenge - Tickets List</h3>
        <table class=table border="1">
            <tr class="thead-dark">
                <th scope="col">ID</th>
                <th scope="col">Subject</th>
                <th scope="col">Requester</th>
                <th scope="col">Status</th>
                <th scope="col">Details</th>
            </tr>
            %for ticket in feedback['tickets']:
                <tr>
                    <td>{{ticket['id']}}</td>
                    <td>{{ticket['subject']}}</td>
                    <td>{{ticket['requester_id']}}</td>
                    <td>{{ticket['status']}}</td>
                    <td><a href="/detalhe/{{ticket['id']}}">Details</a></td>
                </tr>
            %end
        </table>
        <div>
            <ul class="pagination justify-content-center">
                 <li class="page-item"><a class="page-link" href="/more_tickets?url={{feedback['previous_page']}}">Previous</a></li>
                %import math
                %for i in range(1, math.ceil(feedback['count']/25)+1):
                     <li class="page-item"><a class="page-link" href="/more_tickets_byNumber/{{i}}">{{i}}</a></li>
                %end
                <li class="page-item"><a class="page-link" href="/more_tickets?url={{feedback['next_page']}}">Next</a></li>
             </ul>
        </div>
    </form>
</div>



