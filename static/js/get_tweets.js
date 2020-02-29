
console.log('get_tweets.js loaded')

function yourTweets(){

	d3.json('/cleaned_tweets', function(data){
		console.log(data)
		// console.log(data.type())
		return data
	})
}

yourTweets()
// console.log(data)