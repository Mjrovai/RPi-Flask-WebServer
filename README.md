# RPi-Flask-WebServer
Python WebServer with Flask and Raspberry Pi

Let's create a simple WebServer to control things in your home. There are a lot of ways to do that. For this project here, we will use FLASK, a very simple and free microframework for Python. With Flask, will be very simple to control Raspberry GPIOs over the internet.

Flask is called a micro framework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself.

On this tutorial, we will use a Raspberry Pi as a local Web Server, where we will control via a simple webpage, 3 of its GPIOs programmed as outputs (acting as actuators) and monitor 2 of its GPIOs, programmed as inputs (sensors). The block diagram shows what we want to accomplish.
<p> 
<img src=“https://github.com/Mjrovai/RPi-Flask-WebServer/blob/master/Block_Diagram.png”>
</p>
