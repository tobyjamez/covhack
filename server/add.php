<?php
// required headers
header("Content-Type:application/json");

include_once ('db.php');

if(!isset($_POST['name']))
{
  $name=$_POST['name'];
  response(200,"Product",$name);
  $sqlstatement="SELECT itemid FROM items WHERE name LIKE '".$name."' ORDER BY price ;";
  $result = $mysqli->query($sqlstatement);
  $row = mysqli_fetch_assoc($result);

  $itemid = $row['itemid'];

  if(empty($itemid))
  {
    response(200,"Product Not Found",NULL);
  }
  else
  {

    //look in account number 1 for list of object ids
    $sqlstatement1="INSERT INTO basket VALUES ('1',".$itemid.");";
    //return array of object ids
    $result = $mysqli->query($sqlstatement1);

    if(!$result)
    {
      response(200,"Could not add to db",NULL);
    }
    else
    {
      response(200,"Product added to db","Item inserted");
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