function FeatureRequestViewModel() {
    var self = this;

    self.requests = ko.observable();
    self.requestDetail = ko.observable();

    self.submitSuccess = ko.observable();

    self.getRequests = function () {
        self.requestDetail(null);
        $.get('/api/requests/', self.requests);
    };

    self.getRequestDetail = function (request) {
        self.requests(null);
        $.get('/api/requests/' + request.id, self.requestDetail)
    };

    self.deleteRequest = function (message) {
        $.ajax({
            url: '/api/requests/' + message.id,
            type: 'DELETE',
            data: {message: message},
            success: function () {
                self.getRequests();
            }
        });

    };


    self.postRequest = function () {
        $.ajax({
            url: '/api/requests/',
            type: 'POST',
            contentType: "application/json",
            accepts: "application/json",
            dataType: 'json',
            data: JSON.stringify({
                title: 'Add more buttons to the dashboard',
                client: 'Britecore',
                description: 'At this point we have very few buttons. People love buttons, lets add more',
                target_date: '2017-10-10'
            }),
            success: function () {
                self.submitSuccess(true)

            },
            error: function (jqXHR) {
                console.log("POST error: " + jqXHR.status);
            }
        });

    };
    self.getRequests();
}

ko.applyBindings(new FeatureRequestViewModel());