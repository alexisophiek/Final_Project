function yourTweets(){

	d3.json('/get_tweets', function(data){
		console.log('data is... according to get_tweets....')
		console.log(data)
		console.log('data ',data)
		console.log('type is .... ', typeof(data))
		return data
	})
	return data
}



yourTweets()

var tr = d3.select("#tabledump")
     .selectAll("tr")
     .data(data)
     .enter().append("tr");

