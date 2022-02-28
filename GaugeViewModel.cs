using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Gauge
{
  public class GaugeViewModel
  {
    int arcLength_;
    string temp_ = "0";
    public GaugeViewModel()
    {
    }
    public string Temp
    {
      get { return temp_; }
      set { Temp = temp_; }
    }

  }
}
