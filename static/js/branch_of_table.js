var data

function yourTweets(){

	d3.json('/tweets', function(data){
		console.log('data is... according to get_tweets....')
		console.log(data)
		// console.log('data ',data)
		// console.log('type is .... ', typeof(data))
		console.log('first data point in data issss.... . . . . . .','\n',data[0])
		console.log('length of data is . . . ', data.length)

var data = data[0,10]

		var tweets_data = data
		console.log(data)

		var titles = ['text','id']
		// var titles = d3.keys(data[0,1]);

		var table = d3.select('#table').append('table');

		// var table = d3.select('#page-wrap').append('table');
		// var headers = table.append('thead')

		// var hrow = headers.append('tr').enter()
		// .append('td')
		// .text(titles)
							// .enter().append('td')


		// var headers = table.append('thead').append('tr')
		//                    .selectAll('th')
		//                    .data(titles).enter()
		//                    .append('th')
		//                    .text(function (d) {
		// 	                    return d;
		//                     })



		var rows = table.append('tbody').selectAll('tr')
		               .data(data).enter()
		               .append('tr');
		  rows.selectAll('td')
		    .data(function (d) {
		    	return titles.map(function (k) {
		    		return { 'value': d[k], 'name': k};
		    	});
		    }).enter()
		    .append('td')
		    .attr('data-th', function (d) {
		    	return d.name;
		    })
		    .text(function (d) {
		    	return d.value;
		    });
		// var data = data[:20]
		// var data = data[0,10]
		


		// // console.log(titles)
		// var body = table.append('tbody')
		//                .data(data).enter()
		//                .append('tr');
		// var rows = body.selectAll('tbody').append('td').data(data).enter() 
		// // rows.selectAll('td')
		//     // .data(function (data) {
		//     // 	return titles.map(function (k) {
		//     // 		return { 'value': data['data'][k], 'name': k};
		//     // 	});
		//     // }).enter()
		//     .append('td')
		//     .attr('data-th', function (d) {
		//     	return d.name;
		//     })
		//     .text(function (d) {
		//     	return d.value;
		//     });
		// // var text = data['data']['text']

		//   rows.selectAll('td')
		//     // .data(function (d) {
		//     // 	return titles.map(function (k) {
		//     // 		return { 'value': d[k], 'name': k};
		//     // 	});
		//     .data(function (data) {
		// 		// var text = data['data']['text']

		//     	// var text = data['data']['text']
		//     	// console.log(text)
		//     	return titles.map(function (data) {
		//     		// console.log(text)
		//     		// console.log(typeof(text))
		//     		// console.log(typeof(data[text]))
		//     		return { 'value': data[data][text], 'name': data};
		//     	});
		//     }).enter()
		//     .append('td')
		//     .attr('data-th', function (d) {
		//     	return d.name;
		//     })
		//     .text(function (d) {
		//     	return d.value;
		//     });


     		// var headers = table.append('thead').append('tr')
		     //               .selectAll('th')
		     //               .data(titles).enter()
		     //               .append('th')
		     //               .text(function (d) {
			    //                 return d;
		     //                })
		     //               .on('click', function (d) {
		     //            	   headers.attr('class', 'header');
		                	   
		     //            	   if (sortAscending) {
		     //            	     rows.sort(function(a, b) { return b[d] < a[d]; });
		     //            	     sortAscending = false;
		     //            	     this.className = 'aes';
		     //            	   } else {
		     //            		 rows.sort(function(a, b) { return b[d] > a[d]; });
		     //            		 sortAscending = true;
		     //            		 this.className = 'des';
		     //            	   }
		                	   
		     //               });




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