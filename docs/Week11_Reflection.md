🔖 Section 0: Fellow Details
Fill out the table below:

Field	Your Entry
Name	Brenda Alvarez-Lagunas
GitHub Username	balvarez74
Preferred Feature Track	Data / Visual
Team Interest	Yes - Project Owner or Contributor
______

✍️ Section 1: Week 11 Reflection
Answer each prompt with 3–5 bullet points:

Key Takeaways: What did you learn about capstone goals and expectations?
    (1) It's very important to break the project down into digestible bits. This provides clarity due to the more in-depth brainstorming of each part.

    (2) The capstone has 4 components: core, 3 features, enhancement, and team portion

    (3) This project not only provides us with a learning opportunity, but also a portfolio piece (crucial when job hunting)

Concept Connections: Which Week 1–10 skills feel strongest? Which need more practice?
    (1) The skill(s) that feels strongest to me includes:
        - basics of functions (definition and parameters),
        - data structures (dictionaries, sets),
        - module importing,
        - essential programming concepts, including nested data structures.
        - pandas, matplotlib

    (2) The skills I need to practice more on include:
        - exception handling with try-except for debugging (I find this very intimidating),
        - fundamentals of object-oriented programming (OOP) with classes and class methods,
        - basic sorting algorithms (bubble and insertion sort),
        - efficient sorting methods (merge and quicksort),
        - searching techniques (binary and linear search)

Early Challenges: Any blockers (e.g., API keys, folder setup)?
    (1) setting up basic architecture of repo

    (2) setting up the week11_reflection.md file (homework instructions not as clear that the file needs to be in the weather-dashboard-brenda repo, initially, I spent a lot of time browsing through JTC's GitHub library looking for a docs/ folder)

    (3) creating my first repo was also a bit of a blocker but luckily, Patrick Snoop helped us get this setup on Monday or Tuesday of this week

Support Strategies: Which office hours or resources can help you move forward?
    (1) W11D1 - Capstone Introduction - Lesson Slides - https://docs.google.com/presentation/d/1Iz_LN5tMEEY7busgwTyXAOtgNWdMJEteVHv1Ckd8g4U/edit?slide=id.g33d3747ab16_0_102#slide=id.g33d3747ab16_0_102

    (2) Pathways S25 Step-by-Step Guide to the Capstone Project - https://docs.google.com/document/d/1kvKpYdQsoFYvZ0b6GqzzfltmZ862f__eh1r4lvtVWrI/edit?tab=t.dqpkjgq9tv45

    (3) W11D4 Deck - Project Planning - https://docs.google.com/presentation/d/198285P8Q-mWvYME8AYzN8hiTmL0Z6gfYKqlRcMerwds/edit?slide=id.g343ade77ff3_0_21#slide=id.g343ade77ff3_0_21

____

🧠 Section 2: Feature Selection Rationale
List three features + one enhancement you plan to build.

#	Feature Name	Difficulty (1–3)	Why You Chose It / Learning Goal
    (1)	Simple Statistics / 1 / I think I could complete this more easily than other options and realistically speaking, I don't want to burn myself out with this project + full-time job.		

    (2)	Weather History Tracker / 1 / I think I could complete this more easily than other options and realistically speaking, I don't want to burn myself out with this project + full-time job.	

    (3)	Temperature Graph / 2 / I find this one intriguing and fun. Plus helpful to see the weekly/monthly/annual trends.

Enhancement		–	
🧩 Tip: Pick at least one “level 3” feature to stretch your skills!
____

🗂️ Section 3: High-Level Architecture Sketch
Add a diagram or a brief outline that shows:

(1) Core modules and folders
(2) Feature modules
(3) Data flow between components

weather-dashboard-brenda
├── main.py               # Main app logic
├── config.py             # Your API keys
├── features/             # Feature modules
│   └── (empty for now)
├── data/                 # For saved CSV or text files
├── docs/                 # README and user_guide.md
├── requirements.txt      # Will be added in Week 16
└── screenshots/          # Add images for your README

____

📊 Section 4: Data Model Plan
Fill in your planned data files or tables:

File/Table Name	    Format (txt, json, csv, other)	    Example Row
weather_history.txt	    txt	                            2025-06-09,New Brunswick,78,Sunny
weekly_fig.png          png                             graph containing weekly trend
weather_data.csv        csv                             2025-06-09,Tampa,85,Sunny
____

📆 Section 5: Personal Project Timeline (Weeks 12–17)
Customize based on your availability:

Week	Monday	         Tuesday	        Wednesday	    Thursday	 Key Milestone
12	    API setup	     Error handling	    Tkinter shell	Buffer day	 Basic working app
13	    Feature 1	     Integrate	        Feature 1 complete
14	    Feature 2 start	 Review & test	    Finish	        Feature 2 complete
15	    Feature 3	     Polish UI	        Error passing	Refactor	All features complete
16	    Enhancement	Docs Tests	            Packaging	    Ready-to-ship app
17	    Rehearse	     Buffer	            Showcase	–	Demo Day

____
⚠️ Section 6: Risk Assessment
Identify at least 3 potential risks and how you’ll handle them.

Risk	                Likelihood  (High/Med/Low)	Impact (High/Med/Low)	    Mitigation Plan
API Rate Limit	        Medium	                    Medium	                    Add delays or cache recent results
Internet Interuption    High                        High                        Add backup, sample data or error message
Run Out of Time         Med                         High                        Plan accordingly, stick to schedule
____
🤝 Section 7: Support Requests
What specific help will you ask for in office hours or on Slack/Discord?
    (1) how to implement API key while keeping it private
    (2) raise bugs that I am unable to fix or figure out
    (3) if merge conflicts arise, i'll need guidance in navigating this
____

✅ Section 8: Before Monday (Start of Week 12)
Complete these setup steps before Monday:
    ✅ Push main.py, config.py, and a /data/ folder to your repo
    ✅ Add OpenWeatherMap key to .env (⚠️ Do not commit the key)
    TBD Copy chosen feature templates into /features/
    ✅ Commit and push a first-draft README.md
    ✅ Book office hours if you're still stuck on API setup