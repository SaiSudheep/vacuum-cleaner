# vacuum-cleaner
A simple reflexive vacuum cleaner agent for two rooms

Agent starts from Room A:

  ![image](https://github.com/user-attachments/assets/2133f1f3-41b9-4c35-a04c-26777429ade2)

  ![image](https://github.com/user-attachments/assets/0b2f500e-6eea-45bc-8ec7-c922ef9a7288)

Agent starts from Room B:

  ![image](https://github.com/user-attachments/assets/d00e6f61-5272-4038-89a5-7bcc28c3b6e9)

  ![image](https://github.com/user-attachments/assets/0fb10382-9b6f-4980-8727-4fb3e48d9411)

Thus, the overall average scores are,

Total number of moves = 3*8 = 24 moves

Average desirable moves = 3 + 2 + 1 + 0 + 3 + 1 + 2 + 0 = 12 moves

Average unwanted moves = 0 + 1 + 2 + 3 + 0 + 2 + 1 + 3 = 12 moves

<img width="364" alt="image" src="https://github.com/user-attachments/assets/5155b5fe-4653-481d-818b-42cc0e36f869">


Desirable move – A move that the agent is expected to make.

Unwanted move – A move that does not add any value to the environment.

Undesirable move – A move that the agent should not make. For example, if the agent ignores the dirt in its room and moves to the next room, it can be considered as an undesirable move.

To summarize, it is good that we do not have any undesirable moves. This means that the agent is able to successfully complete its tasks. However, it is interesting to note that we have an equal number of desirable and unwanted moves. The agent can be programmed to avoid unwanted moves if it has information about the state of both rooms at the same time.
