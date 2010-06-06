$.getJSON(
	"../tweets.php",
	function(data){
		$.each(data.userdata, function(i,user){
			var friends = user.friends;
			var tweets = user.tweets;
			var users = user.amount; 
			//alert(friends + tweets + users);
		});
		return users;
	}
);
	alert(users);
