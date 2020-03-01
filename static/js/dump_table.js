var data

function yourTweets(){

	resp = d3.json('/tweets', function(data){
		console.log('data is... according to get_tweets....')
		// console.log(data)
		// console.log('data ',data)
		// console.log('type is .... ', typeof(data))
		console.log('first data point in data issss.... . . . . . .','\n',data[0])
		console.log('length of data is . . . ', data.length)
		var tweets_data = data

		var tr = d3.select("#table")
     		.selectAll("tr")
     		.data(data)
     		.enter().append("tr")
     		// .add
		return data
	})
	return data
}

yourTweets()
console.log('type ~ ~ ~ ~ ~ ', typeof data)

// var tr = d3.select("#table")
//      .selectAll("tr")
//      .data(data)
//      .enter().append("tr");

// console.log(data)