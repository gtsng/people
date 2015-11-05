openerp.caller = function(instance, local) {
    var _t = instance.web._t,
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;

    local.HomePage = instance.Widget.extend({
        start: function() {
            console.log("Calls Management Home Page");
        },
    });

    instance.web.client_actions.add('caller.homepage', 'instance.caller.HomePage');
}
