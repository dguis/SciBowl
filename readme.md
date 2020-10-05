# Science Bowl
Current project status: ![Linter](https://github.com/dguis/SciBowl/workflows/Linter/badge.svg) ![Unit Tests](https://github.com/dguis/SciBowl/workflows/Unit%20Tests/badge.svg)

## Overview
An advanced program for science bowl training that will analyze rounds to provide statistics as well as use machine learning to teach players in areas they may not be as familiar.

## Competition Description

> Launched in 1991, the National Science Bowl® (NSB) is a highly competitive science education and academic event among teams of high school and middle school students who compete in a fast-paced verbal forum to solve technical problems and answer questions in all branches of science and math. Each team is composed of four students, one alternate student, and a coach. Regional and national events encourage student involvement in math and science activities of importance to the Department of Energy and the Nation. 

[US DOE Website](https://science.osti.gov/wdts/nsb/About)

  

In this competition, teams compete to answer questions in "rounds" such as the one shown below.

  

![Sample Science Bowl Round](https://s3.studylib.net/store/data/007105732_1-95fa9e81486c14f791ac00873dfef29b.png)

## Problem Statement

The Science Bowl competition covers a large range of subject areas, and it is very difficult to know where to start studying. It is also quite difficult to go through practice questions and study them without another person there to read them to you. Long story short, studying for the competition is a lot of work, and there is currently no simple solution.


## Project Proposal

Many of the tasks that are required for studying content such as reading rounds, figuring out what things are necessary to study, etc. can easily be automated by a computer algorithm. This project will attempt to enhance the process of completing many of these tasks. The main functions of the project will be as follows:

### Steps
1. Extract data from PDF sample rounds
2. Analyze rounds and get statistics on most common topics
3. Display questions on a screen and give the users a time limit to answer them
4. Use some sort of text-to-voice algorithm to actually read the questions, so that it is more similar to an actual competition
5. Generate statistics on what topics individual users need to study
6. Implement machine learning to enhance steps 2 and 6, and to provide a better classification of topic areas
7. Sync with a database to layout what topics each member of a team is good at, and what they each need to study in order to be the most successful in the competition.

 ### Other Possible Features 
- GUI for training
- Display of questions as text
- Auto question reader
- Round selection
- Allow players to choose what rounds/categories they want to play
- Greater customizability
- Specific category selection
- Specific difficulty selection
- Round timers and controls
- Stop reading when buzzed
- Simulate real round
- Buzzer system integration

## Project Design
At this point in time, the project is going to incorporate the following objects:

Main: Responsible for initializing the game, and serving up the GUI to the user. It ties everything all together.
Extractor: This class is in charge of extracting questions from round files (as shown above). It will then move them into a format that includes all of the necessary information to ask a player a given question.
User: Keeps track of information and statistics about the player.
QuestionAsker: This is responsible for formatting the questions properly to be served up in the GUI, or maybe read out loud in the future.
Analyzer: The analyzer takes in the data provided by the user and the extractor, and generates statistics both for the player's strengths and weaknesses, and well as general statistics for all of the rounds.
Database: This object interacts with a database to help store and update data.
GUI: This is pretty self explanatory. Manages the GUI. It may integrate other objects as widgets, but that will come later.

### Interface
This project is going to, in a way, be separated into two different parts. The "Game" portion, and the "Analysis" portion. 

#### Game
The game portion is intended to ask players questions and record information about it. The game program flow may look as follows:
```mermaid
graph TD
Main{Main}
User
GUI
QuestionAsker
Database
Analyzer

Main --> User
Main --> QuestionAsker
User --> QuestionAsker
QuestionAsker --> GUI
QuestionAsker --> Database
GUI --> QuestionAsker
Database --> Analyzer
```
#### Analysis
The analysis portion analyzes the rounds and the game data. Here is what the flow of the analysis side may look like:
```mermaid
graph TD
Database
User
Analyzer
Extractor

Database --> Analyzer
User --> Analyzer
Extractor --> Analyzer
Analyzer --> Database

```

### Complex Program Flow
This is a demo of how the program might function as a whole.
```mermaid
graph TD
Main{Main}
User
GUI
Extractor
QuestionAsker
Analyzer
Database

Main --> GUI
Main --> Extractor
Main --> User
User --> Main
User --> Database
Extractor --> QuestionAsker
Extractor --> Analyzer
QuestionAsker --> GUI
QuestionAsker --> Analyzer
Analyzer --> Database
Analyzer --> GUI
Database --> Main
GUI --> QuestionAsker

```

### CRC Cards

### Object Layout

### More Specific Class Features

### GUI Layout

### GUI Object Layout



## Resources
### Pre-existing options

- [High School Science Bowl Practice](https://play.google.com/store/apps/details?id=com.jakepolatty.highschoolsciencebowlpractice&hl=en_US)

- [Tycho](https://apps.apple.com/us/app/tycho-play-science-quiz-bowl/id1191853690)

- [Protobowl](https://protobowl.com/scibowl/lobby)

  

### Links

- [MS Sample Questions](https://science.osti.gov/wdts/nsb/Regional-Competitions/Resources/MS-Sample-Questions)

- [HS Sample Questions](https://science.osti.gov/wdts/nsb/Regional-Competitions/Resources/HS-Sample-Questions)


<!--stackedit_data:
eyJwcm9wZXJ0aWVzIjoidGl0bGU6IFNjaWVuY2UgQm93bCBQcm
9qZWN0IFByb3Bvc2FsXG5hdXRob3I6IERhbGxpbiBHdWlzdGlc
biIsImhpc3RvcnkiOlstNTI1MTEzNDE4LC0yMDQ3ODU2Mzk3XX
0=
-->