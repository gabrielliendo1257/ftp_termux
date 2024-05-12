package com.data.ftp_protocol.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.data.ftp_protocol.service.CommandService;

@RestController
public class HomeController {

    @Autowired
    private CommandService commandService;

    @GetMapping("/hello")
    public String hello() {
        this.commandService.run("E:\\codes\\python-projects\\projects\\ftp_termux\\server_ftp.py");
        return "Hello World";
    }
}
