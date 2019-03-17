<?php
// required headers
error_reporting(E_ALL);
ini_set("display_errors", 1);

header("Content-Type:application/json");

include_once ('db.php');

//look in account number 1 for list of object ids
$sqlstatement1="SELECT name,price, providerid, itemid FROM items;";
//return array of object ids
$result = $mysqli->query($sqlstatement1);

if(empty($result))
{
	//for each objectid
	//if it finds an instance of itself in the list, add 1 to  quantity
	while($row = mysql_fetch_assoc($result)){
		/*
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
		*/
    $providerid = $row['providerid'];       //providerid

    //Find name of provider
    $sqlstatement3="SELECT provider FROM providers WHERE providerid ='".$providerid."';";
    $providernameresult = $mysqli->query($sqlstatement3);

    if(empty($result)){

	    $providername = mysqli_fetch_assoc($providernameresult);
	    $provider = $providername['provider'];  //contains provider
	    $price = $row['price'];                 //contains price
	    $name = $row['name'];                   //name
	    $itemresponse = array($name, $price,$provider);
	    
	    response(200,"Product Not Found",NULL);
  	}
	  else
	  {
	    response(200,"Product Found",$itemresponse);
	  }
	}
}
else
{
  response(400,"Invalid Request",NULL);
}

function response($status,$status_message,$data)
{
  header("HTTP/1.1 ".$status);
  
  $response['status']=$status;
  $response['status_message']=$status_message;
  $response['data']=$data;
  
  $json_response = json_encode($response);
  echo $json_response;
}

?>