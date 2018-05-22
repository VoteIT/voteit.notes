
function handle_personal_notes(event) {
    var target = $(event.currentTarget);
    var form = target.find('#vote_form');
    if (form.length > 0) {
        var form_url = form.attr('action');
        var pos = form_url.indexOf('/__vote__?')
        if (pos > 0) {
            inject_personal_notes(form_url.slice(0, pos+1), '#vote_form .modal-body:first')
        }
    }
}

function inject_personal_notes(poll_url, body_selector) {
    var request = arche.do_request(poll_url + 'personal_notes_for_poll');
    request.done(function(response) {
        $(body_selector).before(response);
    });
}

$(function() {
    $('body').on('shown.bs.modal', '#modal-area', handle_personal_notes);
});
