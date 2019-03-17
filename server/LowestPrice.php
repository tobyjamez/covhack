<?php

//Input, will eventually be through post

$json = file_get_contents("php://input");
$obj = json_decode($json); //obj should be renamed name and nect line removed
$name = "apple";
if(!is_string($obj)){
    throw new Exception('Received content contained invalid JSON!');
}

$sqlstatement="SELECT name, price, itemid, providerid FROM items WHERE name LIKE '".$name."'ORDER BY price ;";

$url = getenv('JAWSDB_URL');
$dbparts = parse_url($url);

$hostname = $dbparts['host'];
$username = $dbparts['user'];
$password = $dbparts['pass'];
$database = ltrim($dbparts['path'],'/');

//opening the mySQL database and ordering items by price
$mysqli = new mysqli($hostname, $username, $password, $database);
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

//create response json
$response = array();
$response["name"] = $name;
$response["price"] = $price;
$response["provider"] = $provider;
$jsonDataEncoded = json_encode($response);

//API Url to send back to
$url = 'http://example.com/api/JSON/create';
 
//Initiate cURL.
$ch = curl_init($url);
 
//Tell cURL that we want to send a POST request.
curl_setopt($ch, CURLOPT_POST, 1);
 
//Attach our encoded JSON string to the POST fields.
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonDataEncoded);
 
//Set the content type to application/json
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json')); 
 
//Execute the request
$result = curl_exec($ch);

?>