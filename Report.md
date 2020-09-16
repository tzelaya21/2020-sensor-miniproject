{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Overview"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The Fall 2020 sensor miniproject was based on the simulation of internet-connected sensors. Simulated sensors are used to test proposed designs against impairments including delayed, missing or incorrect data. The IoT simulator consists of a Websockets server that emits data packets with random timing to the backend client."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Procedure"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Platforms used in this Project"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Ubuntu Terminal (WSL)\n",
    "* Jupyter Notebook\n",
    "* Pandas and NumPy was used in task 2 & 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Task 0 \n",
    "First I cloned the MiniProject2020 repository from github. Then I created the IoT server using server.py. After this created the client using client.py. Both codes were run simultaneously for a considerably longer time and data packets for three different rooms were collected containing the following information\n",
    "1. Room\n",
    "2. CO2\n",
    "3. Occupancy\n",
    "4. Temperature\n",
    "5. Time"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Task 1\n",
    "The data packets being recieved were in JSON format were stored in a .Json file, by adding the following lines of code in client.py file\n",
    "![code snippet](4.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Then data was saved in the following format\n",
    "![code snippet](5.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Task 2\n",
    "For the first three questions of task 2, the room **Lab1** was selected. Answer to all the four questions of task2 were obtained using the code provided in **Task2.py**\n",
    "![Solution to Q1, Q2 & Q3(Temperature Graph)](7.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![Q3(CO2 Graph)](8.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![Q3(Occupancy Graph)](9.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![Solution to Q4)](10.png)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Task 3\n",
    "We were asked to remove all the bad **Temperature Data Points** from the room selected in Task2. I did so by letting go off all the data points outside two standard deviation from the mean temperature. The new median and variance were calculated by using the remain valid data points.\n",
    "![Code Snippet)](11.png)\n",
    "\n",
    "Also, a persistent change in temperature doesn't always indicate a fualty sensor. It might be that the temperature is actually changing."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Conclusion\n",
    "* As the simulation generates truly random sensor values at random time intervals for three rooms but in random order which depicts the behaviour of the real world.\n",
    "* First of all this simulation is deficient of **Real Hardware** (Hence the name simulation). It fails to account for the probability of any sensor being faulty or not working at all. What kind of data would be recieved in that scenario? \n",
    "* Python Websockets library is far more easy to use as compared to C++ Websockets. There are many in-built which saves time and brains which we had to write in C++. \n",
    "* In my opinion, the latter option is better because it incorporates the urgency and the very purpose of IoT. If the server was polling the sensors after a set amount of time, there will always be a bigger load while retrieving the data from the sensors."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
