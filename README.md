# MediMap

## About 
<P>Term: Fall 2025
<P>Team: Team Sky
<P>Students : Adla Nitish,
              Bandi Mallikarjuna,
              Dasari Venkata Sai Aditya Nischal, 
              Garapati Kranthi Swapna.

#️⃣ **Keywords**:  
Large Language Model (LLM), Natural Language Processing (NLP), Query Understanding, Intent Extraction, Entity Recognition, Conversational AI, Multi-Criteria Optimization,Ranking Algorithm, Gradient Boosting.

## 💻 Project Abstract:  

MediMap is an innovative Large Language Model (LLM)-powered healthcare navigator designed to simplify the process of scheduling diagnostic tests. The system addresses key patient challenges, including lack of price transparency, unclear insurance coverage, and difficulty finding available appointments. By allowing users to submit natural-language queries, MediMap intelligently parses requests, retrieves data from facility databases, and employs a multi-criteria ranking algorithm to generate personalized recommendations. The expected outcome is a functional prototype that reduces patient effort, improves cost and insurance transparency, and provides a scalable foundation for future expansion into broader healthcare services.

### 🫧 Background
Trying to book a medical scan like an MRI is frustrating. No one shows prices upfront, it's unclear what insurance covers, and finding an available appointment takes hours of phone calls.
This delay causes unnecessary stress and can push back important diagnoses.MediMap was created to solve this. We use AI to understand your simple question, like "find a cheap MRI near me with my insurance," and instantly find you the best options. It turns a complicated, stressful process into one that takes seconds.

## High Level Requirement: MediMap

1.  Talk to it: You can ask for what you need in your own words.
2.  See prices & insurance: It shows you the cost and what insurance is accepted.
3.  Find appointments: It finds places with available times.
4.  Get the best match: It sorts the results to show you the top options first.
5.  Book it: It gives you a way to schedule your appointment.

### 📋 Functional Requirements: MediMap
1. User Query & Interaction  
      1.1: The system shall provide a text input field for users to enter a natural language query.  
      1.2: The system shall provide a button to submit the query and initiate the search.  
      1.3: The system shall allow users to grant permission to access their location for "near me" searches.  
      1.4: The system shall display a clear and concise summary of the parsed query back to the user for confirmation (e.g., "Finding: Cheapest MRI near Seattle with Premera insurance").  

2. Data Processing & Search  
    2.1: The system shall parse the user's query to accurately identify the required medical test (e.g., MRI, CT Scan).  
    2.2: The system shall parse the user's query to identify the location parameter (e.g., city, zip code, "current location").  
    2.3: The system shall parse the user's query to identify the priority criterion (e.g., "cheapest," "closest," "soonest").  
    2.4: The system shall parse the user's query to identify a specified insurance provider.  
    2.5: The system shall search the internal database for facilities that match the test type and location.  
    2.6: The system shall filter results based on insurance acceptance and availability.  

3. Results & Ranking  
    3.1: The system shall display search results in a ranked list, ordered by the user's specified priority.  
    3.2: The system shall display each result with at least: Facility Name, Address, Distance, Price Estimate, Insurance Match, and Next Available Appointment.  
    3.3: The system shall provide a visual map view showing the geographic location of all matching facilities.  
    3.4: The system shall allow users to sort the results by different criteria (Price, Distance, Availability) after the initial search.  
    3.5: The system shall allow users to select and compare up to 3 facilities side-by-side in a table.  

4. Booking & Actions  
      4.1: For each result, the system shall provide a clear call-to-action button (e.g., "Book Now", "See More Times").  
      4.2: The booking action shall redirect the user to the facility's official booking page OR display a simulated booking form within the application.  
      4.3: The system shall allow users to share a facility's details via email or a generated link.  

5. System Management (Admin)  
      5.1: Administrators shall be able to add, edit, and deactivate facilities in the database.  
      5.2: Administrators shall be able to trigger a manual refresh of data from external APIs (e.g., to update availability). 

###  ✅ Non functional Requirements

Other minor requirements and considerations like Cloud deployable solution etc.

### ✍🏼 Conceptual Design

Of course. Here is a conceptual design for MediMap based on our previous discussions.

### **Conceptual Design: MediMap**

**1. Vision**
MediMap is an AI-powered agent that automates the entire process of finding and booking medical appointments. It acts as a personal assistant that handles the phone calls, calendar checks, and scheduling logistics based on a simple voice command from the user.

**2. Core Concept: The Agentic Workflow**
The system's intelligence comes from an AI Agent that doesn't just answer questions—it takes action. It dynamically decides which tools to use and in what sequence to complete the user's request from start to finish.

**3. High-Level Architecture**
The design follows a modern, cloud-native architecture built for security and scalability:
- **Frontend:** A Progressive Web App (PWA) that provides a voice-first interface, works on any device, and can be installed like a native app.
- **Backend:** A Python-based API layer that orchestrates the process, leveraging LangChain to manage the AI agent's reasoning and tool use.
- **AI Core:** A large language model (e.g., GPT-4) serves as the "brain," interpreting requests and planning actions.
- **Tools via MCP:** Separate, secure servers (Model Context Protocol) provide the agent with capabilities like accessing calendars, searching for providers, and making phone calls without exposing sensitive API keys.
- **Cloud Infrastructure:** The entire system is deployable on scalable cloud services (e.g., AWS, GCP) using Infrastructure-as-Code, ensuring reliability and maintainability.

**4. Key Differentiator**
Unlike simple chatbots, MediMap is an action-taking agent. The user provides a goal ("I need a dentist appointment"), and the system autonomously executes the multi-step process to achieve it, only returning to the user for final confirmation.

This design prioritizes a seamless user experience, robust security for handling sensitive health data, and a modular architecture that allows for easy updates and integration of new tools and services.

### 🛠️ Technical Design
<P>Lorem ipsum odor amet, consectetuer adipiscing elit. Tellus nunc vulputate ornare dignissim faucibus accumsan per; pretium ante. Fringilla aptent posuere conubia ut montes urna a quis. Ligula mattis venenatis platea venenatis, scelerisque porttitor habitant orci etiam. Sodales pharetra libero sit sed libero cras nostra suscipit. Quam massa vivamus; orci turpis rhoncus vestibulum ullamcorper habitasse. Magnis feugiat conubia lacinia, mauris ac lacinia eget conubia aliquet. Laoreet viverra aptent dictum nascetur arcu velit maximus ridiculus ligula. </P>
<P>Lorem ipsum odor amet, consectetuer adipiscing elit. Tellus nunc vulputate ornare dignissim faucibus accumsan per; pretium ante. Fringilla aptent posuere conubia ut montes urna a quis. Ligula mattis venenatis platea venenatis, scelerisque porttitor habitant orci etiam. Sodales pharetra libero sit sed libero cras nostra suscipit. Quam massa vivamus; orci turpis rhoncus vestibulum ullamcorper habitasse. Magnis feugiat conubia lacinia, mauris ac lacinia eget conubia aliquet. Laoreet viverra aptent dictum nascetur arcu velit maximus ridiculus ligula. </P>

### 📦 Required Resources

Linux Development Machine
Raspberry Pi Pico W
Mobile Application Development Environment
IDE/Text Editor
Project Management (Jira)
Version Control management (GitHub/Git)
Database (MYSQL)
PyTorch
Jupyter


### Project Plan :  
<P>Lorem ipsum odor amet, consectetuer adipiscing elit. Tellus nunc vulputate ornare dignissim faucibus accumsan per; pretium ante. Fringilla aptent posuere conubia ut montes urna a quis. Ligula mattis venenatis platea venenatis, scelerisque porttitor habitant orci etiam. Sodales pharetra libero sit sed libero cras nostra suscipit. Quam massa vivamus; orci turpis rhoncus vestibulum ullamcorper habitasse. Magnis feugiat conubia lacinia, mauris ac lacinia eget conubia aliquet. Laoreet viverra aptent dictum nascetur arcu velit maximus ridiculus ligula. </P>


## 🏁 Milestones 

List the important deliverables and milestones with dates
| Date/Week | Milestone  | Deliverables/Features |
|---------|-----------|----------------------------------|
| Week 1 | Scope/Spec | Define project objectives and scope  |
| Week 2 | Spec | Define and finalize specifications |
| Week n | abcd  | Deploy and demo  |




### 🧪 Test Cases
<P>Lorem ipsum odor amet, consectetuer adipiscing elit. Tellus nunc vulputate ornare dignissim faucibus accumsan per; pretium ante. Fringilla aptent posuere conubia ut montes urna a quis. Ligula mattis venenatis platea venenatis, scelerisque porttitor habitant orci etiam. Sodales pharetra libero sit sed libero cras nostra suscipit. Quam massa vivamus; orci turpis rhoncus vestibulum ullamcorper habitasse. Magnis feugiat conubia lacinia, mauris ac lacinia eget conubia aliquet. Laoreet viverra aptent dictum nascetur arcu velit maximus ridiculus ligula. </P>
<P>Lorem ipsum odor amet, consectetuer adipiscing elit. Tellus nunc vulputate ornare dignissim faucibus accumsan per; pretium ante. Fringilla aptent posuere conubia ut montes urna a quis. Ligula mattis venenatis platea venenatis, scelerisque porttitor habitant orci etiam. Sodales pharetra libero sit sed libero cras nostra suscipit. Quam massa vivamus; orci turpis rhoncus vestibulum ullamcorper habitasse. Magnis feugiat conubia lacinia, mauris ac lacinia eget conubia aliquet. Laoreet viverra aptent dictum nascetur arcu velit maximus ridiculus ligula. </P>

### 👩🏻‍🏫 Installation Instructions

These instructions are to help build and run the project locally on your system.

#### Minimum Requirements

In order to install and build this project you must have (at the time of this being written):

  a MacOS machine
  MacOS Sonoma 14.4 as the minimum version
  XCode 15 minimum (XCode can be downloaded from the App Store)
  iPhone Simulator with iOS 17.0 minimum (XCode will download this for you), or iPhone with iOS 17.0 minimum
  if using a physical iPhone, it can be connected via cable with the Mac machine.
  A valid iCloud Account
  iCloud Account should also have at 10kb of free storage remaining.
  The steps to building and running the project:

    git clone <this repo git link>
    Open XCode and click on open existing project
    Locate the project and select the SmartWeights.xcodeproj file.
    This file will have the AppStore icon.
    Select your target location to run the project through the dropdown at the time of the IDE.
    It will likely say any iOS device (arm64) the first time
    Press the play/start the active scheme button found in the top left of the IDE.
    Testing


### 👩🏻‍💻🧑🏻‍💻 Collaborators

[//]: # ( readme: collaborators -start )
<table>
<tr>
    <td align="center">
        <a href="https://github.com/digitaldiv">
            <img src="https://avatars.githubusercontent.com/u/1842870?v=4" width="100;" alt="Div Pithadia"/>
            <br />
            <sub><b>Div Pithadia</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/chargershub">
            <img src="https://avatars.githubusercontent.com/u/160267476?v=4" width="100;" alt="Chargers hub"/>
            <br />
            <sub><b>Chargers Hub</b></sub>
        </a>
    </td></tr>
</table>

[//]: # ( readme: collaborators -end )


