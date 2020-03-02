
console.log('data is loading')

function model_df(){

	d3.json('/cleaned_tweets', function(data){
		console.log(data)
		return data
	})
}

model_df()