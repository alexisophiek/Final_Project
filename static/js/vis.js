var dates = []
	var dateStrings = []
	var sumEmotions
	var allSums = []
	var x = []
	var y = []
var data 
var emoList
var feels = []
var sentiments = ['negative', 'positive']
var emotions = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']
var anger, anticipation, disgust, fear, joy, sadness, surprise, trust
var negative, positive
/*PREFERRED ROUTE AS OF TODAY*/  
function emoTweets(){
	d3.json('/emotions_and_tweets', function(d){
		/*
		THIS NOW PROVIDES ONLY THE DICTIONARIES
		*/
		var nrcList = ["anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust", "negative", "positive"]
		var readyData = {}
		data = d.data
		// 
			for (var i = 0; i < data.length; i++) {
				sumEmotions = 0
				if (isNaN(data[i]['emotion_dictionaries']['anger'])) {
					anger = 0
				}
				else{
					anger = data[i]['emotion_dictionaries']['anger']
				}
				// 
				// 
				// console.loganger))
				// if (true) {}
				// anticipation = data[i]['emotion_dictionaries']['anticipation']
				// disgust = data[i]['emotion_dictionaries']['disgust']
				// fear = data[i]['emotion_dictionaries']['fear']
				// joy = data[i]['emotion_dictionaries']['joy']
				// sadness = data[i]['emotion_dictionaries']['sadness']
				// surprise = data[i]['emotion_dictionaries']['surprise']
				// trust = data[i]['emotion_dictionaries']['trust']
				// negative = data[i]['emotion_dictionaries']['negative']
				// positive = data[i]['emotion_dictionaries']['positive']
				if(isNaN(data[i]['emotion_dictionaries']['anticipation'])) {
					anticipation = 0
				}
				else{
					anticipation = data[i]['emotion_dictionaries']['anticipation']
				}
				if(isNaN(data[i]['emotion_dictionaries']['disgust'])) {
					disgust = 0
				}
				else{
					disgust = data[i]['emotion_dictionaries']['disgust']
				}
				if(isNaN(data[i]['emotion_dictionaries']['fear'])) {
					fear = 0
				}
				else{
					fear = data[i]['emotion_dictionaries']['fear']
				}
				if(isNaN(data[i]['emotion_dictionaries']['joy'])) {
					joy = 0
				}
				else{
					joy = data[i]['emotion_dictionaries']['joy']
				}
				if(isNaN(data[i]['emotion_dictionaries']['sadness'])) {
					sadness = 0
				}
				else{
					sadness = data[i]['emotion_dictionaries']['sadness']
				}
				if(isNaN(data[i]['emotion_dictionaries']['surprise'])) {
					surprise = 0
				}
				else{
					suprise = data[i]['emotion_dictionaries']['surprise']
				}
				if(isNaN(data[i]['emotion_dictionaries']['trust'])) {
					trust = 0
				}
				else{
					trust = data[i]['emotion_dictionaries']['trust']
				}
				if(isNaN(data[i]['emotion_dictionaries']['negative'])) {
					negative = 0
				}
				else{
					negative = data[i]['emotion_dictionaries']['negative']
				}
				if(isNaN(data[i]['emotion_dictionaries']['positive'])) {
					positive = 0
				}
				else{
					positive =  data[i]['emotion_dictionaries']['positive']
				}
				sumEmotions = (anger + anticipation + disgust + fear + joy + sadness + surprise + trust + negative + positive)
				anger_score = (anger / sumEmotions)
				anticipation_score = (anticipation / sumEmotions)
				disgust_score = (disgust / sumEmotions)
				fear_score = (fear / sumEmotions)
				joy_score = (joy / sumEmotions)
				sadness_score = (sadness / sumEmotions)
				surprise_score = (surprise / sumEmotions)
				trust_score = (trust / sumEmotions)
				negative_score = (negative / sumEmotions)
				positive_score = (positive / sumEmotions)
				readyData = {'anger_score': anger_score, 
					'anticipation_score': anticipation_score, 
					'disgust_score': disgust_score,
					'fear_score': fear_score, 
					'joy_score': joy_score, 
					'sadness_score': sadness_score, 
					'surprise_score': surprise_score,
					'trust_score': trust_score,
					'negative_score': negative_score,
					'positive_score':positive_score}
					console.log(readyData.positive_score)
				x.push(readyData.positive_score)
				y.push(readyData.trust_score)
			}
var trace1 = {
  x: x,
  y: y,
  mode: 'markers',
  type: 'scatter'}
//   marker: {
// 		size: 30,
// 		color: 'rgba(217, 217, 217, 0.14)'
// 		// line: {
// 		// color: 'rgba(217, 217, 217, 0.14)',
// 		//	width: 0.5},
// 		//opacity: 0.8}
// };
console.log(trace1)
var layout = {
	  xaxis: {
	  	range: [-.1, 1.5],
	    autotick: false,
	    ticks: 'outside',
	    tick0: 0,
	    dtick: .05,
	    ticklen: 2,
	    tickwidth: 1,
		tickcolor: '#000'
	  },
	  yaxis: {
	  	range: [-.1, 1.5],
	    autotick: false,
	    ticks: 'outside',
	    tick0: 0,
	    dtick: .05,
	    ticklen: 2,
	    tickwidth: 1,
	    tickcolor: '#000'
	  },
	  fill: "transparent"
		};
var data = [trace1]
Plotly.newPlot('vis', data, layout);
		})
	}
emoTweets()
