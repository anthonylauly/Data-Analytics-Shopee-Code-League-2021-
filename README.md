# Data-Analytics-Shopee-Code-League-2021-

This Repository contain my submission of Data Analytic competition. The task is to gather all contacts available in specific Ticket. An example<br><br>

Ticket A <br>  

Id | 0  
--- | ---
Email | John@gmail.com
Phone | NA  
Order ID | 12345678
Contacts | 5

Ticket B <br>

Id | 1 
--- | --- 
Email | NA
Phone | 682212345  
Order ID | 12345678
Contacts | 2

Ticket C<br>

Id | 34567 
--- | --- 
Email | Wick@gmail.com
Phone | 682212345  
Order ID | NA
Contacts | 4

Ticket D<br>

Id | 78999 
--- | --- 
Email | Wick@gmail.com
Phone | NA  
Order ID | NA
Contacts | 3

Each of these tickets are related either directly or indirectly through Email, Phone or Order ID,therefore each ticket belongs to the same user.<br>
● Ticket A and B are linked through Order ID<br>
● Tickets B and C are linked through Phone<br>
● Tickets C and D are linked through Email<br>
● Tickets A and D are indirectly linked through tickets A > B > C > D <br><br>

This query is important for the RCR matrix (Repeat Contact Rate) which is a measure of customer service.
