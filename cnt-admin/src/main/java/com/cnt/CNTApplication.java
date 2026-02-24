package com.cnt;





import org.springframework.boot.SpringApplication;


import org.springframework.boot.autoconfigure.SpringBootApplication;


import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;





/**


 * 启动程序


 * 


 * @author CNT


 */


@SpringBootApplication(exclude = { DataSourceAutoConfiguration.class })


public class CNTApplication


{


    public static void main(String[] args)


    {


        // System.setProperty("spring.devtools.restart.enabled", "false");


        SpringApplication.run(CNTApplication.class, args);


        System.out.println("  \n" );



    }


}


