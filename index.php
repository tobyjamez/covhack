<?php 
$name = "apple";

$sqlstatement="SELECT name, price, itemid, providerid FROM items WHERE name LIKE '".$name."'ORDER BY price ;";

include_once ('server/db.php');

$result = $mysqli->query($sqlstatement);

//Get relevant data about item
$row = mysqli_fetch_assoc($result);
$price = $row['price'];
$itemid = $row['itemid'];
$providerid = $row['providerid'];

//Find name of provider
$sqlstatement1="SELECT provider FROM providers WHERE providerid =".$providerid.";";
$providernameresult = $mysqli->query($sqlstatement1);
$providername = mysqli_fetch_assoc($providernameresult);
$provider = $providername['provider'];
echo $provider;
?>