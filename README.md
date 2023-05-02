# CS333-FinalProject
- Created by: Charlotte Moreland
- Date: 5/1/23
- Class: CS 333
- Assignment: Final Project


Build and Test Infrastructure:
- To build and test the code one just needs to push the code to the Github repository
- From the repository there are Github actions in place to automatically test and build the code
- To access these tests one just needs to visit the Github actions segment of the repository and click
- on the version of python they would like to see to view more details and see if the tests passed

Build and Deployment Infrastructure:
- The build and deploy the code there is a yml file in place in the Github workflows folder
- This yml will run the dockerfile that is in place in the repository in order to build
- the docker image for deployment. Thus, all the user must do it run the docker image on their
- machine in order to use the program. For the user input to be usable the user must run the 
- docker image with the command -it in order to see the correct program function.
