# FAQ

- URL: https://knowledgebase.webengage.com/docs/segments-faq
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

FAQ
Commonly asked questions related to creating and analyzing segments in WebEngage
1. How can I create a rolling segment?
Rolling segments are just a concept that guides the creation of a segment and is not a type of segment as such.
For example, let’s say you create a segment which is to include all users who last opened your mobile app 7 days ago. This segment, by nature, becomes a rolling segment as users will roll in and out of it as and when their actions match the parameter,
last seen equals more than 7 days
.
2. How can I create a segment in which a few locations are included and a few excluded?
Currently, the WebEngage dashboard does not extend the functionality of clubbing locations by the logic of inclusion and exclusion, while creating a segment.
You can either choose to club multiple locations by the logic of inclusion
(including all users located within the specified regions)
or by the logic of exclusion
(excluding all users located within the specified regions)
.
3. How do I check which users have performed a certain event using segments?
To see if a specific set of users have performed a particular event, you can create a segment that includes only those users who have performed the action on your app/website. This can be done by adding behavioral parameters when creating a segment in your dashboard.
Detailed read
.
4. What is the difference between a user based segment and an event-based segment?
The difference between a user based segment and an event-based segment is that the former includes users based on user attributes like
last seen, purchase value, channel reachability preferences, location, etc.
- while the latter includes users based on the events performed / not performed by the users.
5. Why is the status of a segment,
In Progress?
The status,
In Progress
indicates the time taken by WebEngage to create a new segment.
Once you hit the
Save
button, depending on the parameters set by you, it may take some time for WebEngage to populate the segment. Segments which include users based on their behavior (events data), take longer to populate than segments which include users based on generic information like their
location, last date and time of interaction, reward points, purchase value and so on.
6. Can I create a segment based on
Event Time?
Yes! You can create a segment based on the time an event was performed. This can be done by selecting the desired event
(under behavioral parameters when creating a segment)
and adding time as an attribute filter.
7. Can I analyze a segment of users against the events they have performed?
Currently, the WebEngage dashboard does not extend the functionality of analyzing users over the events they may have performed and vice versa. Don’t be disheartened; our tech geniuses are working hard to make this possible shortly :)
We hope that you have found an answer to all your queries here. Please feel free to drop in a few lines at
[email protected]
in case you have any queries or feedback, we're always just an email away!
Updated
7 months ago
Predictive Segments
Data Management
Copy Page
