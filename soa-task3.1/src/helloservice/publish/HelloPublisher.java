package helloservice.publish;

import javax.xml.ws.Endpoint;

import helloservice.Hello;

public class HelloPublisher {
    public static void main(String[] args) {
        Endpoint.publish("http://localhost:8088/hello", new Hello());
    }
}