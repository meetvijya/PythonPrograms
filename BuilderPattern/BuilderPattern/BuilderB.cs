using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BuilderPattern
{
    class BuilderB:IBuilder
    {
        Product _product = null;
        public void DoIt()
        {
            _product = new Product("Builder B");
        }

        public string GetProductName
        {
            get
            {
                return _product.GetProductName();
            }
        }
    }
}
