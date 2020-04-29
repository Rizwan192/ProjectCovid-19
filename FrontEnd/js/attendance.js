
document.getElementById("detailed_content").style.visibility = "hidden";
function attendance() {
	var s_id = document.getElementById("id").value;
	//alert("bef" + s_id);
	var basic_content = ''
	var final_content = '';
	var table_content = '';
	var content = '';
	content = content + '<div style="font-size: 16pt" class="alert alert-danger" role="alert">';
	if (s_id == '') {
		document.getElementById("id").style.borderColor = "red";
		content = content + '<strong>Fill Out </strong>The Field! </div> ';
		document.getElementById("alert_there").innerHTML = content;
	}
	else {
		basic_content = '';
		basic_content = basic_content + '<table class="table table-striped" border="2">';
		basic_content = basic_content + '<thead class="thead-light">';
		basic_content = basic_content + '<tr class="bg-success">';
		basic_content = basic_content + '<th scope="col">Ser No.</th>';
		basic_content = basic_content + '<th scope="col">Name</th>';
		basic_content = basic_content + '<th scope="col">Timestamp</th>';
		basic_content = basic_content + '<th scope="col">Other Present</th>';
		basic_content = basic_content + '  </tr>';
		basic_content = basic_content + ' </thead>';
		basic_content = basic_content + '<tbody>';
		var c = 1;
		var s_username;
		var s_timestamp;
		var match_timestamp;
		var other;
		var rootRef = firebase.database().ref();
		var urlRef = rootRef.child('stickynote-3a600/Live_Tracking/');
		urlRef.once("value", function (snapshot) {
			snapshot.forEach(function (child) {
				s_username = child.val().p_name;
				if (s_username == s_id) {
					alert(s_timestamp);
					s_timestamp = child.val().p_timestamp;
					var rootRef2 = firebase.database().ref();
					var urlRef2 = rootRef2.child('stickynote-3a600/Live_Tracking/');
					urlRef2.once("value", function (snapshot) {
						snapshot.forEach(function (child) {
							{
								match_timestamp = child.val().p_timestamp;
								if (s_timestamp == match_timestamp) {
									other = child.val().p_name;
									alert(other);
									table_content = table_content + '<tr>';
									table_content = table_content + '<td>' + c + '</td>';
									table_content = table_content + '<td>' + s_username + '</td>';
									table_content = table_content + '<td>' + match_timestamp + '</td>';
									table_content = table_content + '<td>' + other + '</td>';
									table_content = table_content + '</tr>';
									final_content = final_content + '</tbody>';
									final_content = final_content + '</table>';
									document.getElementById("table_content").innerHTML = basic_content + table_content + final_content;
									final_content = '';
									var content = '';
									content = content + '<div style="font-size: 16pt" class="alert alert-success" role="alert">';
									content = content + '<strong>Data </strong>Found! </div> ';
									document.getElementById("alert_there").innerHTML = content;
									c = c + 1;
								}
							}
						});
					});
				}
			});
		});
	}
}