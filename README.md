# Seyyed & Amin Calculator
Computer Networking Project number 1 - Shahid Beheshti University

Simple Calculator handled in Server-Client format with python

## Requirements
Any version of Python 3


## Discription
This program is to send simple calculation requests from a client. Server handles the Calculation and returnes the result with exec time.


## Usage

### As server (Seeder)

To run:

`python server.py`

Just run server and let it be.


### As Client

`python client.py`

After running the client, you can send calculation requests in the following format:

`$ Add $ 5 $ 7 $`

* Add
* Subtract
* Divide
* Multiply

And,

`$ Sin $ 6 $`

* Tan
* Sin
* Cot
* Cos

Result will be returned in the following format:

`$ Time $ Result $`

which:
* **Time** is the exec. time
* **Result** is the result of calcuation
