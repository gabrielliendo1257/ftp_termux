package com.data.ftp_protocol.service;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import org.springframework.stereotype.Service;

@Service
public class CommandService {

    public void run(String command) {
        try {
            // Crear proceso
            ProcessBuilder builder = new ProcessBuilder();
            builder.command("python", command); // Para sistemas tipo Unix
            // builder.command("cmd.exe", "/c", comando); // Para sistemas Windows

            // Redirigir la salida del proceso
            builder.redirectErrorStream(true);

            // Ejecutar proceso
            Process proceso = builder.start();

            // Obtener la salida del proceso
            BufferedReader reader = new BufferedReader(new InputStreamReader(proceso.getInputStream()));
            String linea;
            while ((linea = reader.readLine()) != null) {
                System.out.println(linea); // Puedes hacer algo con la salida, como loguearla o devolverla como
                                           // resultado
            }

            // Esperar a que el proceso termine
            int exitCode = proceso.waitFor();
            System.out.println("Proceso finalizado con código de salida: " + exitCode);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
