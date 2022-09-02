create database BankDB;
use BankDB;
create table bank_2
(ACC_NO bigint(15) primary key,
NAME varchar(20),
MOBILE bigint(15),
EMAIL varchar(40),
ADDRESS varchar(30),
CITY varchar(20),
COUNTRY varchar(20),
BALANCE bigint(15));
insert into bank_2 values
(5642980764, 'BINOD THARU' ,6767676767, 'binodtharu67@gmail.com','ANDHERE EAST' , 'MUMBAI','INDIA',15090); 
insert into bank_2 values
(5642980765, 'ABHINAV GUPTA',3457698790,'abhinavgupta9@outlook.com','DAWARIKA' , 'NEW DELHI' ,525560);
insert into bank_2 values
(5642980766 , 'RAM MISHRA',9876876456, 'rammishra@gmail.com','BANDRA', 'MUMBAI', 'INDIA' , 109567);
INSERT INTO bank_2 VALUES 
(5642980767 ,'ADARSH SINGH' ,7896578543, 'adarshsingh@rediffmail.com', 'MALAD' ,'MUMBAI' , 'INDIA', 5645990);
INSERT INTO bank_2  VALUES 
(5642980768 , 'MUKESH AMBANI' ,9079899456, 'mukeshambani@gmail.com', 'BORIVELLI', 'MUMBAI','INDIA', 76490768965);
insert into bank_2 values
(5642980769 , 'NEHA MISHRA' , 8790453256 , 'nehamishra@yahoomail.com' , 'TOWN HALL' ,'MUMBAI' , 'INDIA' , 189306);
insert into bank_2 values
(5642980770 , 'PAHUL PREET' , 5987914567 , 'pahulpreet@outlook.com' , 'POWAI', 'MUMBAI' , 'INDIA' , 1598435);
insert into bank_2 values
(5642980771 , 'DHAYAN CHANDRA' , 8912539871 , 'dhayanchandra@rediffmail.com' , 'TOWN HALL', 'PUNE' , 'INDIA' , 857492);
insert into bank_2 values
(5642980772 , 'AKASH NAIR' , 9415298745 , 'akashnair@outlook.com' , 'MARINE LINE','MUMBAI' , 'INDIA' ,2198457);
insert into bank_2 values
(5642980773 , 'RATAN TATA' , 9450367867 , 'ratantata@gmail.com' ,'KALYAN', 'MUMBAI' , 'INDIA' , 5789139879);
insert into bank_2 values
(5642980774 , 'CAMILA CABELLO' , 5987456313 , 'camilacabello@gmail.com' ,'MATUNGA ROAD', 'MUMBAI' , 'INDIA' , 120467396); 
insert into bank_2 values
(5642980775 , 'JAMES ARTHUR' , 4908019415 , 'jamesarthur@outlook.com' , 'VETAL HILL' ,'PUNE' , 'INDIA' , 219860478);
insert into bank_2 values
(5642980776 , 'SELENA GOMEZ' , 4987879469 , 'selenagomez@gmail.com' , 'HIRANANDANI', 'MUMBAI' , 'INDIA' , 106969);
insert into bank_2 values
(5642980777 , 'SHAWN MENDES' , 6983569746 , 'shawnmendes@yahoo.com' , 'GOREGOUN', 'MUMBAI' , 'INDIA' , 41975);
insert into bank_2 values
(5642980778 , 'SHAKURA ALI' , 9785614598 , 'alishakura@rediffmail.com' ,'SOUTH GOA', 'GOA' , 'INDIA' , 10987);
insert into bank_2 values
(5642980779 , 'ASIM KHAN' , 7698569785 , 'asimkhan@hotmail.com' , 'TOWN HALL ','PUNE' , 'INDIA' , 98037);
insert into bank_2 values
(5642980780 , 'MAMTA SHUKLA' , 9504559829 , 'mamtashukla987@outlook.com' ,'DAWARIKA', 'NEW DELHI' , 'INDIA' , 928603);
insert into bank_2 values
(5642980781 , 'AASHMA ALI' , 9504896434 , 'aashmaali123@outlook.com' , 'DAWARIKA' ,'NEW DELHI' , 'INDIA' , 189358);
insert into bank_2 values
(5642980782 , 'HUGHE ALEBRTO' , 8976796458 , 'albertohughe@gmail.com' , 'NORTH GOA ', 'GOA' , 'INDIA' , 1754947);
SELECT * FROM bank_2;




