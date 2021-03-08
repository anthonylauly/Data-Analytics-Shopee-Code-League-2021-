# Data-Analytics-Shopee-Code-League-2021-

This Repository contain my submission of Data Analytic competition. The task is to gather all contacts available in specific Ticket. An example<br><br>

Ticket A                          <br>                    
+-----------+-------------------+<br>                     
| Id&ensp;        |   0&ensp;               |<br>
+-----------+-------------------+<br>
| Email     |   John@gmail.com  |<br>
+-----------+-------------------+<br>
| Phone     |   NA              |<br>
+-----------+-------------------+<br>
| Order ID  |   12345678        |<br>
+-----------+-------------------+<br>
| Contacts  |   5               |<br>
+-----------+-------------------+<br><br>

Ticket B <br>
+-----------+-------------------+<br>
| Id        |   1               |<br>
+-----------+-------------------+<br>
| Email     |   NA              |<br>
+-----------+-------------------+<br>
| Phone     |   682212345       |<br>
+-----------+-------------------+<br>
| Order ID  |   12345678        |<br>
+-----------+-------------------+<br>
| Contacts  |   2               |<br>
+-----------+-------------------+<br><br>

Ticket C<br>
+-----------+-------------------+<br>
| Id        |   34567           |<br>
+-----------+-------------------+<br>
| Email     |   Wick@gmail.com  |<br>
+-----------+-------------------+<br>
| Phone     |   682212345       |<br>
+-----------+-------------------+<br>
| Order ID  |   NA              |<br>
+-----------+-------------------+<br>
| Contacts  |   4               |<br>
+-----------+-------------------+<br><br>

Ticket D<br>
+-----------+-------------------+<br>
| Id        |   78999           |<br>
+-----------+-------------------+<br>
| Email     |   Wick@gmail.com  |<br>
+-----------+-------------------+<br>
| Phone     |   NA              |<br>
+-----------+-------------------+<br>
| Order ID  |   NA              |<br>
+-----------+-------------------+<br>
| Contacts  |   3               |<br>
+-----------+-------------------+<br><br>

Each of these tickets are related either directly or indirectly through Email, Phone or Order ID,therefore each ticket belongs to the same user.<br>
● Ticket A and B are linked through Order ID<br>
● Tickets B and C are linked through Phone<br>
● Tickets C and D are linked through Email<br>
● Tickets A and D are indirectly linked through tickets A > B > C > D <br><br>

This query is important for the RCR matrix (Repeat Contact Rate) which is a measure of customer service.
