using System;
using System.Windows;

namespace Gauge
{
  public class GaugeViewModel
  {
    int arcLength_;
    int radius_ = 150;
    Point center_ = new(200,200);
    string temp_ = "0";
    Point arcEnd_ = new(210,275);
    public GaugeViewModel()
    {
      arcEnd_.X = center_.X + (radius_ * Math.Cos(Math.PI));
      arcEnd_.Y = center_.Y + (radius_ * Math.Sin(Math.PI));
    }
    public string Temp
    {
      get { return temp_; }
      set { Temp = temp_; }
    }
    public Point ArcEnd
    {
      get { return arcEnd_; }
      set { ArcEnd = arcEnd_; }
    }

  }
}
