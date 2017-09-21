function FeatureRequestViewModel() {
    var self = this;

    self.title = ko.observable();
    self.description = ko.observable();
    self.client = ko.observable();
    self.target_date = ko.observable();
    self.priority = ko.observable();

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
                title: self.title(),
                client: self.client(),
                description: self.description(),
                target_date: self.target_date(),
                priority: self.priority()
            }),
            success: function () {
                self.submitSuccess(true);
                self.getRequests();
            },
            error: function (jqXHR) {
                console.log("POST error: " + jqXHR.status);
            }
        });

    };
    self.getRequests();
}

ko.applyBindings(new FeatureRequestViewModel());