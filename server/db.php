<?php 
$url = getenv('JAWSDB_URL');
$dbparts = parse_url($url);

$hostname = $dbparts['host'];
$username = $dbparts['user'];
$password = $dbparts['pass'];
$database = ltrim($dbparts['path'],'/');

//opening the mySQL database and ordering items by price
$mysqli = new mysqli($hostname, $username, $password, $database);
?>