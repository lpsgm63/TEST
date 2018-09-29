<?php
$id=$_POST['id'];
$pw=$_POST['pw'];
if(preg_match('/\'/',$id)){
	try{
		echo 'tt';
		$db = new PDO('mysql:host=localhost;dbname=honey','catiless','12345');
		$db->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
		$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		$query = 'select id from login where id = :id and passwd = :pw';
		$tmp = $db->prepare($query) or die($db->errorInfo());
		$tmp->bindParam(':id',$id,PDO::PARAM_STR);
		$tmp->bindParam(':pw',$pw,PDO::PARAM_STR);
		$tmp -> execute();
		$result = $tmp->fetchAll(PDO::FETCH_NUM);
		for($i = 0; $i < count($result); $i++) {
			printf( "%s login success!!!! <br />", $result[$i]);
		}
	} catch (PDOException $e){
		print $e->getMessage();
		return false;
		$db = null;
	}
}
else{
	try{
		$db = new PDO('mysql:host=localhost;dbname=main','catiless','12345');
		$db->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
		$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		$query = 'select id from login where id = :id and passwd = :pw';
		$tmp = $db->prepare($query) or die($db->errorInfo());
		$tmp->bindParam(':id',$id,PDO::PARAM_STR);
		$tmp->bindParam(':pw',$pw,PDO::PARAM_STR);
		$tmp -> execute();
		$result = $tmp->fetchAll(PDO::FETCH_NUM);
		for($i = 0; $i < count($result); $i++) {
			printf ("%s login success!!!! <br />", $result[$i]);
		}
	} catch (PDOException $e){
		print $e->getMessage();
		return false;
	}
	$db = null;
}




