# Club management system (different from club website make generic)
Description: We want a application that allows us to handle different aspects of managing a club. We want it super generic so that it can be
customizable to anyone.

# Five Main Aspects:

## President and Vice-President:
- In this section of the application, we want to have services that pertain to the president and vice-president roles. A few things we want is an admin page. 
- In this admin page we want to have a task manager, which shows of tasks that we may have to do for the club. 
- We also want to have a section that can show us comments, concerns, recommendations, or feedback that is given to us from the general body. 
- As well as a way to track members who may have not shown up. 
- We want a page that allows us to see members skills and their interests
- We want a page that allows use to give achievements/recognition to members

## Secretary:
- In this section of the application, we want to have services that pertain to the secretary position of the club. 
- In this section, we want to have a page that the secretary can fill out a form. This form should follow the sample minutes, so that it can create a minutes word doc based off the meeting that happens.
- This form should be saved in a .docx format or a .pdf format, and should be saved in the S3 bucket file system. (Extra Feature: once this doc/pdf gets put in the bucket, then have a trigger that sends it out to the minutes@easternct.edu email).
- In this section, we want a way for the secretary to also track the attendence of members that are apart of the club.
- In this section we also want a way for the secretary to send out emails to people who are apart of our email list, instead of manually doing it.

## Treasury:
- In this section of the application, we want to have services that pertain to the treasurer position of the club.
- In this section we want to have a page/dashboard that shows where we are at in the budget for the club.
- In this section we want to have a place that can also show what our next monthly expense is (upcoming monthly subscriptions), as well as a way to find out if we are about to exceed our budget for the semester/month

## Public Relations Officer:
- In this section of the application we want to have services that pertain to the public relations officer position of the club
- In this section we want a page for the PR officer to be able to create events by using a dashboard.
- In this section we also want a way for the PR officer to be able to send out emails if there are any new events (that is not the normal meeting)
- In this section we want a way for the PR officer to also check feedback from the club
- In this section we also want a way that could allow the PR officer to send out surveys out to the club.

## General Body:
- In this section of the application we want to have services that pertain to the general body of the club.
- We want a page that allows the general body to check current events that may be happening with the club like a calendar
- We want a page that shows the location of where the club is located, and when it is happening
- We want a page that has documentation and tutorials
- We want a page that allows members to add their skills and interests
- We want a page that allows members to add ideas/feedback/suggestions either as anonymous or with their name
- We want a page that allows members to check in for a meeting
- In this section, the general body and e-board members can also access it
- A way to track current tasks (idk if this is possible tbh but worth a shot)

## In General:
- In this section of the application we want to have services that's for the entire club, member or not
- We want a page that allows users to log in if they are a member.
- In this page we want a section that allows users to see what project we are currently working on, dream/goal of the club, and what we do in the club
- We want a page that shows achivements/recognition of people and the club
- We want a page that allows us to see Club Alumni, and as well as connect with them
- We want a page that allows people to play PacMan using faces of the E-Board

# Pages to Design (66 Pages in total/33 in total if not counting mobile):
## President and Vice President Pages
- P/VP Dashboard page: displays a summary of upcoming tasks, member attendance, feedback, and achievements
- Member Skils and Interests Page (Admin View): Display members' skill ands interests
- Achievements and Recognition Page (Admin View): A list of members who have recieved achievements with ability to add new recognitions
- Page to add and remove member: Admin controls to manage membership list, adding or removing members
- Task manager page: Dynamic page that allows P/VP to assign tasks, set deadlines, and track progress on tasks (different from GitHub)
- Member Attendance Tracking: View member attendance history and generate reports
- Feedback & Recommendations Page: feedback form or message board where members can submit converns or suggestions
## Secretary Pages
- Secretary Dashboard page: overview of tasks, meeting minutes, attendance, and emails to be sent
- Minutes Form Fillout Page
- Attendance tracker page: A page for tracking attendance at meetings and events
## Treasury Pages
- Treasury Dashboard page: Summary of current funds, expenenses, and upcoming transactions
- Page to add info (i.e. money, next subscrption, current budget): Forms to add income, record expenses, and monitor budget limits
- Detailed budget breakdown page: View a breakdown of current and future expenses (e.g., subscriptions, and club purchases)
- Transaction history page: A detailed list of all financial tranasctions (e.g., expenses, deposits)
## Public Relations Officer Pages
- PR Officer Dashboard Page: Overview of upcoming events, surveys, and feedback.
- Page to Create Events: Form to create events, including date, location, and description, and send notifications.
- Page to Create Surveys: A page for PR officers to create surveys and polls for the club, including multiple question types.
- Feedback Page: Display feedback and suggestions from club members, with the option to mark issues as addressed.
## General Body Pages
- General Body Dashboard Page: Overview of club activities, upcoming meetings, and events.
- Current Events Page: Display upcoming events, including event details (time, date, and location).
- Club Location Page: Show the physical location of club meetings or events (map integration).
- Documentation Page: Access onboarding documentation, tutorials, and club guidelines.
- Skills and Interests Page (Member View): Form for members to add and update their skills and interests.
- Suggestions Page: Page where members can submit ideas or feedback, either anonymously or with their name attached.
- Member "Settings" Page: Allow members to update their personal information (name, email, password) and preferences.
- Meeting Check-in Page: A page for members to check in for meetings and events.
- Member Profile Page: A personal profile page showing the member’s achievements, attendance, and projects.
- Survey Page: be able to look at surveys, and answer them
## In General
- Member Log In Page: Secure login page for members to authenticate.
- Current Project, Dream/Goal of Club, What We Do in Club Page: Informational page about the club’s ongoing projects, mission, and vision.
- Achievements and Recognition of People and Club Page: A page showcasing club milestones and individual member achievements.
- Club Alumni Page: Display information about alumni and allow for alumni connections (e.g., LinkedIn integration).
- PacMan Page: Interactive page where users can play PacMan using the E-board’s faces as characters.
- Notifications Page: A unified place for club members to view all notifications (events, new posts, achievements).

## Enhancements:
- Mobile-Friendly Pages: Ensure that all pages are responsive for mobile users. (+33 pages)
- Notifications
- Search Functionality: Add search functionality across platform for quick acess to events, feedcback, members, and documents

# Templates:

## Example Template:
![image](https://github.com/user-attachments/assets/53ae653c-851d-45c8-b486-d3dd89c215db)

## Example Mobile Template:
![image](https://github.com/user-attachments/assets/ac4f7f63-9658-4516-b95c-af2d972c03fa)

## Example Admin Template
![image](https://github.com/user-attachments/assets/2351d288-34ec-4a53-804d-4d9f540d5233)

## Example Admin Mobile Template
![image](https://github.com/user-attachments/assets/a1403c98-1752-43cb-8be8-0a390477d515)

