odoo.define('pos_payment_ref.models', function (require) {
"use strict";

    var models = require('point_of_sale.models');

    models.load_fields("pos.payment.method", "pos_payment_ref");

    // Payments
    var _super_paymentline = models.Paymentline.prototype;
    models.Paymentline = models.Paymentline.extend({
        init_from_JSON: function (json) {
            _super_paymentline.init_from_JSON.apply(this, arguments);
            this.payment_ref = json.payment_ref;
        },
        export_as_JSON: function () {
            return _.extend(_super_paymentline.export_as_JSON.apply(this, arguments), {
                payment_ref: this.payment_ref,
            });
        },
    });

    //Orders
    var _super_Order = models.Order.prototype;
    models.Order = models.Order.extend({
        add_paymentline_with_details: function(payment_method, infos) {
            this.assert_editable();
            var newPaymentline = new models.Paymentline({},{order: this, payment_method:payment_method, pos: this.pos});
            $.extend(newPaymentline, infos);

            if(payment_method.is_cash_count !== true || this.pos.config.iface_precompute_cash){
                newPaymentline.set_amount( Math.max(this.get_due(),0) );
            }
            this.paymentlines.add(newPaymentline);
            this.select_paymentline(newPaymentline);
        },

    });

});