# python-crash-course from Google at Coursera

Initial state:
python -m venv venv
pip install wheel, toml

Week4 requirements

Module test
Question 1
The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y". The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long. For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.

Question 2
The highlight_word function changes the given word in a sentence to its upper-case version. For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line?

Question 3
A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom. Drew was the first one to note which students arrived, and then Jamie took over. After the class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse order. Complete the steps to combine them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.

Question 4
Use a list comprehension to create a list of squared numbers (n*n). The function receives the variables start and end, and returns a list of squares of consecutive numbers between start and end inclusively.
For example, squares(2, 3) should return [4, 9].

Question 5
Complete the code to iterate through the keys and values of the car_prices dictionary, printing out some information about each one.

Question 6
Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, with names of their friends and how many guests each friend is bringing. Each dictionary is a partial list, but Rory's list has more current information about the number of guests. Fill in the blanks to combine both dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, if a name is included in both dictionaries. Then print the resulting dictionary.

Question 7
Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces, numbers, or punctuation. Upper case should be considered the same as lower case. For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.


WEEK 5 - Object-Oriented Programming (OOP)

Quiz 1
Question 2
Creating new instances of class objects can be a great way to keep track of values using attributes associated with the object. The values of these attributes can be easily changed at the object level.  The following code illustrates a famous quote by George Bernard Shaw, using objects to represent people. Fill in the blanks to make the code satisfy the behavior described in the quote.

Question 3
The City class has the following attributes: name, country (where the city is located), elevation (measured in meters), and population (approximate, according to recent statistics). Fill in the blanks of the max_elevation_city function to return the name of the city and its country (separated by a comma), when comparing the 3 defined instances for a specified minimal population. For example, calling the function for a minimum population of 1 million: max_elevation_city(1000000) should return "Sofia, Bulgaria".

Question 5
We have two pieces of furniture: a brown wood table and a red leather couch. Fill in the blanks following the creation of each Furniture class instance, so that the describe_furniture function can format a sentence that describes these pieces as follows: "This piece of furniture is made of {color} {material}"

Week6

Problem statement and conversion to a user story:
Imagine that you're an IT specialist working in a medium-sized company, your manager wants to create
a daily report that tracks the use of machines. Specifically, she wants to know which users are currently connected to which machines, it's your job to create the report. In your company, there's a system that collects every event that happens on the machines on the network.
Among the many events collected it records each time a user logs in or out of a computer.
With this information, we want to write a script that generates
a report of which users are logged in to which machines at that time.
Before we jump into solving that problem, we need to know what information we'll use as
input and what information we'll have as output. We can work this out by looking at the rest
of the system where our script will live. In our report scenario, the input is a list of events,
each event is an instance of the event class. An event class contains the date when the event happened,
the name of the machine where it happened, the user involved, and the event type. In this scenario, we care about the login and logout event type. All right, that's good to know. But we need to know exact names of the attributes, otherwise, we won't be able to access them. The attributes are called date,
user, machine, and type. The event types are strings and the ones we care about are login and logout.
With that we should have enough information about the input of our script. Our script will receive a list of event objects and we'll access the events attributes. We'll then use that information to know
if a user is currently logged into a machine or not. Let's talk about the output.
We want to generate a report that lists all the machine names and for each machine,
lists of the users that are currently logged in. We then want this information printed on the screen.
We've been tasked with generating a report and we can decide exactly how we want that report to look.
One option would be to print the name of the machine at the beginning of the line and then
list the current users on separate lines and indent it to the right, or we could print
the machine name followed by a colon and then the usernames separated by commas all in the same line,
and we can probably come up with something even more fancy. When formatting a report,
it's easy to get caught up in the making it look good part. I've fallen into that trap but what really
matters is how well the script solves the problem. So it's better to first focus on making the program work. You can always spend time making the report look nice later. Let's keep it simple for now
and we'll go with the approach of printing the machine name followed by all the current users separated by commas. Okay, we now have a pretty good idea of what we need to do. We've identified our problem statement which is we need to process a list of event objects using their date, type, machine, and user attributes to generate a report that lists all users currently logged into the machines. We're off to a great start. The next step we're going to do is some research to work out how to best actually do this.

1: A manager wants a report of what users are logged into all machines.
2: She collects a list of login/logout events for all machines in the shop.
3: Each event has date/time, event type(login or logout), machine name, user name
4: The event are sorted in chronological order and a the list of machines followed by the logged in users follows Example: 

Events:
11/18/2022 08:25:01 login  webserver1.local Jim
11/18/2022 09:25:01 logout webserver1.local Jim
11/18/2022 08:32:01 login  mainserver1.local Susan
11/18/2022 10:25:01 login  webserver1.local Sam
11/18/2022 23:25:01 login  mailserver1.local Fred
11/18/2022 23:26:01 logout mailserver1.local Fred
11/18/2022 13:30:01 login  webserver5.local Jim
11/18/2022 08:25:01 login  webserver1.local Fred

Should produce this report:
mainserver1.local: Susan, Sam, Fred
webserver1.local: Fred, Sam
webserver5.local: Jim

5: Machines are skipped in there's nobody is logged in.