#include "grimecleaner.h"
#include "ui_grimecleaner.h"
//#include <iostream>
//#include <vector>
//#include <stdio.h>
#include <exception>


QString header = "This simple utility is for users that are perhaps not as computer savy as they wished to be. "
        "This program will launch and or help you install software that will make your maintance easier. "
        "It will also guide you in how to use that software.  Think of this as a middle man until you can "
        "do it on your own.  The tabs will only be function for each respective operating system. "
        "So mac users stay on the mac tab and windows users do the same. :) Have a good day.";

grimeCleaner::grimeCleaner(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::grimeCleaner)
{
    ui->setupUi(this);


    connect(ui->installsoftwareButton, SIGNAL(clicked()), this, SLOT(install_software()));
    connect(ui->spybotButton, SIGNAL(clicked()), this, SLOT(open_spybots()));
    connect(ui->malwarebytesButton, SIGNAL(clicked()), this, SLOT(open_malwarebytes()));
    connect(ui->ccleanerButton, SIGNAL(clicked()), this, SLOT(open_ccleaner()));
    connect(ui->prefetchButton, SIGNAL(clicked()), this, SLOT(clean_prefetch()));
    connect(ui->diskcleanupButton, SIGNAL(clicked()), this, SLOT(launch_diskcleanup()));


}

grimeCleaner::~grimeCleaner()
{
    delete ui;

}



int windows_counter = 0;
void grimeCleaner::install_software(){

    ui->textEdit->setText("If You don't have the software listed click on this button again to download installers from the internet. "
                   " <p style=color:blue><b>Software:</b> Spybots, Malwarebytes, Ccleaner.</p>");
    if(windows_counter == 1) {
        system("start http://download.cnet.com/Spybot-Search-Destroy/3000-8022_4-10122137.html");
        system("start http://www.piriform.com/ccleaner/download");
        system("start http://www.malwarebytes.org/lp/lp4/?gclid=CI2-z_DN6rwCFa1lOgodNnsAWg");

    }
    windows_counter++;
}

void grimeCleaner::open_spybots(){
    ui->textEdit->setText("<p>1) Check for updates (bottom left).</p> <p>2) Click on the Check System button (upper left).</p> <p>3) click start a scan. 4) If items are found make sure all are selected and select the fix/delete button.</p>");
    system("cmd /c start C:\\\"Program Files (x86)\"\\\"Spybot - Search & Destroy 2\"\\SDWelcome.exe");
}

void grimeCleaner::open_malwarebytes(){
    ui->textEdit->setText("<p>1) Check for updates.</p> <p>2) Run Scan on the button.</p> <p>3) If results found make sure all are seleted and select fix all.</p>");
    system("cmd /c start C:\\\"Program Files (x86)\"\\\"Malwarebytes' Anti-Malware\"\\mbam.exe");
}

void grimeCleaner::open_ccleaner(){
    ui->textEdit->setText("<p>1) In CCleaner on the botton left click Run Cleaner.</p> <p>2) On the left sie of CCleaner click on the Registry tab.</p> <p>3) Click on Scan for Issues located on the bottom of the program.</p> <p>4) If issues are found click on Fix Selected Issues. Make Sure all Issues are Selected. <div style=color:red>DO NOT BACKUP WHEN ASKED TO.</div></p>");
    system("cmd /c start C:\\\"Program Files\"\\CCleaner\\CCleaner64.exe");

}
int p_counter = 0;
void grimeCleaner::clean_prefetch(){

    ui->textEdit->setText("Please Click the button one more time to clean the prefetch,"
                            " this should only be done once a month as it slows the system down temporarily, however spyware likes to"
                            " hide in this folder.");
    if(p_counter == 1){
    try{
    system("del /Q C:\\Windows\\Prefetch *");
    } catch(std::exception e) {
        QString error = e.what();
        ui->textEdit->setText(error + " Try running the program as an administrator.");
    }
        ui->textEdit->setText("Prefetch folder cleaned!");
    }
    p_counter++;
}


void grimeCleaner::launch_diskcleanup(){
    ui->textEdit->setText("This will automatically launch disk clean up on your main harddrive");
    try{
    system("C:\\windows\\cleanmgr.exe /d<c>");
    } catch(std::exception e) {
        QString error = e.what();
        ui->textEdit->setText(error);
    }
}
