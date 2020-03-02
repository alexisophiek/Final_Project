console.log('~ ~  ~ ~ ~ vis.js connected ~  ~ ~ ')
	var dates = []
	var dateStrings = []
	var sum
	var allSums = []

var data 
var emoList
var feels = []
var emoList
var sentiments = ['negative', 'positive']
var emotions = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']

var nrcList = ["anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust", "negative", "positive"]

console.log(nrcList)

var anger, anticipation, disgust, fear, joy, sadness, surprise, trust
var negative, positive

function emoTweets(){
	d3.json('/emotions_and_tweets', function(d){
		data = d['data']

		function aggValues(data, emoList, nrcList){
			console.log(data[0])
			console.log(emoList[0])
			for (i = 0; i < data.length; i++) {
				sum = 0
				var tweet = data[i]
				var tweetText = data[i]['tweet']
				emoList = data[i]['emotion_dictionaries']
				var emo_trust = emoList['trust']

				for(var el in emoList ) {
						sum += parseFloat(emoList[el]);
				}

				allSums.push(sum)

			for (var i = 0; i < emoList.length; i++) {
				var em = emoList[i]
				var sin_count = Object.keys(emoList)
				console.log(sin_count)
			}
				// getEmotionalScore(emoList, 'trust')
				return emoList
			}
			console.log(allSums)
			return AllSums
		}
		aggValues(data)
		console.log(emoList)

		function getEmotionalScore(emoList, nrcList){
			for (i = 0; i < nrcList.length; i++) {
				var em = nrcList[i]
			}
					
					var feels =  Object.keys(emoList)
					console.log(feels)
					console.log('emoList - - ', emoList)
					// var nrc_emo = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']
					console.log('emoList.em - - ', emoList.em)

					// var score = data.emotion_dictionaries[x]
					// var score = emoList.em
					
					for(i = 0; i < emoList; i++){
						console.log(emoList[i])
						var score = emoList.em
					}
					console.log(score)
					return score
				}
		getEmotionalScore(emoList, anger)


		for(i = 0; i < emoList; i++){
			console.log(emoList[i])
		} 
	  return sum, allSums
	})
	var em = 'trust'
	// getEmotionalScore(emoList, em)
	return allSums
}

emoTweets()

function yourTweets(){
	console.log('running tweets func . . . ')

	d3.json('/tweets_', function(data){

		expected = data['data'][1]
		console.log(typeof(expected))
		console.log(typeof(expected['data']))
		console.log(expected)

		unexpected = data['data'][2503]
		console.log(typeof(unexpected))
		console.log(typeof(unexpected['data']))
		console.log(unexpected)

	for (i = 0; i < data.length; i++) {
		var time = data[i]['data']['timestamp_ms']
		time = parseInt(time * 1000)
		var dateObj = new Date(time * 1000)

			var hours = dateObj.getUTCHours();
			var minutes = dateObj.getUTCMinutes(); 
			var seconds = dateObj.getUTCSeconds();
			var formattedTime = hours.toString().padStart(2, '0') + ':' +  
			                minutes.toString().padStart(2, '0') + ':' +  
			                seconds.toString().padStart(2, '0'); 
		
						dates.push(formattedTime)
	}
					console.log(dates)
					return data
					})
				}

var vis = d3.select('#vis')

var trace1 = {
  x: [],
  y: [],
  mode: 'markers',
  type: 'scatter'
};

Plotly.newPlot('vis', data);
