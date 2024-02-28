
from frappe import _

def get():
	return {
		_("تطبيق الأموال (الأصول)"): {
			_("الأصول الحالية"): {
				_("المدينون"): {_("المدينون"): {"account_type": "Receivable"}},
				_("الحسابات البنكية"): {"account_type": "Bank", "is_group": 1},
				_("النقد في الخزينة"): {_("النقد"): {"account_type": "Cash"}, "account_type": "Cash"},
				_("القروض والسلف (الأصول)"): {
					_("سلف الموظفين"): {},
				},
				_("الأوراق المالية والودائع"): {_("مبلغ عربون"): {}},
				_("أصول المخزون"): {
					_("البضائع في اليد"): {"account_type": "Stock"},
					"account_type": "Stock",
				},
				_("أصول الضرائب"): {"is_group": 1},
			},
			_("الأصول الثابتة"): {
				_("معدات رأس المال"): {"account_type": "Fixed Asset"},
				_("المعدات الإلكترونية"): {"account_type": "Fixed Asset"},
				_("الأثاث والتجهيزات"): {"account_type": "Fixed Asset"},
				_("معدات المكتب"): {"account_type": "Fixed Asset"},
				_("المصانع والآلات"): {"account_type": "Fixed Asset"},
				_("المباني"): {"account_type": "Fixed Asset"},
				_("البرمجيات"): {"account_type": "Fixed Asset"},
				_("الاهلاك المتراكم"): {"account_type": "Accumulated Depreciation"},
				_("حساب الأعمال الرأسمالية قيد الإنشاء"): {"account_type": "Capital Work in Progress"},
			},
			_("الاستثمارات"): {"is_group": 1},
			_("الحسابات المؤقتة"): {_("الافتتاحية المؤقتة"): {"account_type": "Temporary"}},
			"root_type": "Asset",
		},
		_("المصاريف"): {
			_("المصاريف المباشرة"): {
				_("مصروفات البضائع"): {
					_("تكلفة البضائع المباعة"): {"account_type": "Cost of Goods Sold"},
					_("المصروفات المدرجة في تقييم الأصول"): {"account_type": "Expenses Included In Asset Valuation"},
					_("المصروفات المدرجة في التقييم"): {"account_type": "Expenses Included In Valuation"},
					_("تعديلات المخزون"): {"account_type": "Stock Adjustment"},
				},
			},
			_("المصاريف غير المباشرة"): {
				_("المصروفات الإدارية"): {},
				_("عمولة على المبيعات"): {},
				_("الاهلاك"): {"account_type": "Depreciation"},
				_("مصروفات الترفيه"): {},
				_("تكاليف الشحن والتوصيل"): {"account_type": "Chargeable"},
				_("المصروفات القانونية"): {},
				_("مصروفات التسويق"): {"account_type": "Chargeable"},
				_("مصروفات متنوعة"): {"account_type": "Chargeable"},
				_("صيانة المكاتب"): {},
				_("إيجار المكاتب"): {},
				_("المصروفات البريدية"): {},
				_("الطباعة والأدوات المكتبية"): {},
				_("تقريب الأرقام"): {"account_type": "Round Off"},
				_("الراتب"): {},
				_("مصروفات المبيعات"): {},
				_("مصروفات الهاتف"): {},
				_("مصروفات السفر"): {},
				_("مصروفات المرافق"): {},
				_("تكبير/تصغير الخسائر"): {},
				_("الربح/الخسارة عند بيع الأصول"): {},
			},
			"root_type": "Expense",
		},
		_("الإيرادات"): {
			_("الإيرادات المباشرة"): {_("المبيعات"): {}, _("الخدمات"): {}},
			_("الإيرادات غير المباشرة"): {"is_group": 1},
			"root_type": "Income",
		},
		_("مصدر الأموال (المطالبات)"): {
			_("المطالبات الحالية"): {
				_("الدائنون"): {"account_type": "Payable"},
				_("مرتبات الموظفين المستحقة"): {},
			},
			"root_type": "Liability",
		},
		_("حقوق الملكية"): {
			_("رأس المال"): {"account_type": "Equity"},
			_("أرباح المساهمين المدفوعة"): {"account_type": "Equity"},
			_("رصيد الافتتاح"): {"account_type": "Equity"},
			_("الأرباح المحتجزة"): {"account_type": "Equity"},
			"root_type": "Equity",
		},
	}