<?php
// required headers

header("Content-Type:application/json");

include_once ('db.php');

//look in account number 1 for list of object ids
$sqlstatement1="SELECT itemid FROM basket;";
//return array of object ids
$result = $mysqli->query($sqlstatement1);

if(!empty($result))
{
	//for each objectid
	//if it finds an instance of itself in the list, add 1 to  quantity
	while($row = mysqli_fetch_assoc($result)){
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
    $itemid = $row['itemid'];       //providerid

    //Find name of provider
    $sqlstatement3="SELECT name , providerid , price FROM items WHERE itemid = ".$itemid.";";
    $iresult = $mysqli->query($sqlstatement3);

    if(!empty($iresult)){

	    $currentItem = mysqli_fetch_assoc($iresult);
	    $providerid = $currentItem['providerid'];
			$sqlstatement4="SELECT provider FROM providers WHERE providerid =".$providerid.";";
    	$iresult2 = $mysqli->query($sqlstatement4);	
    	$currentItem2 = mysqli_fetch_assoc($iresult2);    
    	$provider= $currentItem2['provider'];
	    																							  //contains provider
	    $price = $currentItem['price'];                 //contains price
	    $name = $currentItem['name'];                   //name
	    $itemresponse = array($name, $price,$provider);
	    response(200,"Product Found",$itemresponse);
  	}
	  else
	  {
	    response(200,"Product Not Found",NULL);
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