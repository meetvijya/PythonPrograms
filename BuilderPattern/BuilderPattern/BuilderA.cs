using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BuilderPattern
{
    class BuilderA:IBuilder
    {
        Product _product = null;
        public void DoIt()
        {
            _product = new Product("BUilderA");  
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
