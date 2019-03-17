<?php

//Input, will eventually be through post

$json = file_get_contents("php://input");
$obj = json_decode($json); //obj should be renamed name and nect line removed
$name = "apple";
$response = array(); //This is the response to the json file

$action = $obj->action; //action defines the porton of code to run
$word = $obj->word;   //This has a function dependent on the action

if( $action == "search") {
    //Find all instances of the word we are looking for in database
    $sqlstatement="SELECT name, price, itemid, providerid FROM items WHERE name LIKE '".$name."'ORDER BY price ;";
    //opening the mySQL database and ordering items by price
    $mysqli = new mysqli("localhost", "root", "", "groceries1");
    $result = $mysqli->query($sqlstatement);
    //create array of prices and provider
    while($row = mysql_fetch_assoc($result)){
        $price = $row['price'];                 //contains price
        $itemid = $row['itemid'];               //item id
        $providerid = $row['providerid'];       //providerid
    
        //Find name of provider
        $sqlstatement1="SELECT provider FROM providers WHERE providerid =".$providerid.";";
        $providernameresult = $mysqli->query($sqlstatement1);
        $providername = mysqli_fetch_assoc($providernameresult);
        $provider = $providername['provider'];  //contains provider
        
        //append these to arrays to response
        $searchresponse = array(price, itemid, provider);
        array_push($response, $searchresponse);
    }
    //send response back
}
else if( $action == "add") {
    //get object id and find it
    $userid = 1;
    
    INSERT INTO BASKET (basketid, itemid)
        //below $word should be given as a itemid
        VALUES ($userid, $word);    
    //add this to a 'basket' in user ID
}
else if ( $action == "show" ) {
    //look in account number 1 for list of object ids
    $sqlstatement1="SELECT name,price, providerid, itemid FROM items;";
    //return array of object ids
    $result = $mysqli->query($sqlstatement1);
    
    //for each objectid
    //if it finds an instance of itself in the list, add 1 to  quantity
    while($row = mysql_fetch_assoc($result)){
        $itemid = $row['itemid'];
        //go through each object id in items, looks for them in the array
         $sqlstatement2="SELECT itemid FROM basket;";
         $result2 = $mysqli->query($sqlstatement2);
         $index = 0;
         while($row2 = mysql_fetch_assoc($result2)){
            if($row2[$itemid] == $row[$itemid]) {
                $index += 1;
    
            }
         }
        $providerid = $row['providerid'];       //providerid
    
        //Find name of provider
        $sqlstatement1="SELECT provider FROM providers WHERE providerid =".$providerid.";";
        $providernameresult = $mysqli->query($sqlstatement1);
        $providername = mysqli_fetch_assoc($providernameresult);
        $provider = $providername['provider'];  //contains provider
        $price = $row['price'];                 //contains price
        $name = $row['name'];                   //name
        $itemresponse = array($name, $price,$provider);
        
        array_push($response, $itemresponse);
    }
    //return array of arrays {name; price; provider}
    //return the names, prices and providers of the object IDs in basket
}


//REQUIRED CODE
//encodes and sends back response
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