using System;
using System.Drawing;
using System.Drawing.Printing;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;
using System.Windows.Shapes;
using Brushes = System.Windows.Media.Brushes;
using Point = System.Windows.Point;
using Size = System.Windows.Size;

namespace Gauge
{
  /// <summary>
  /// Interaction logic for MainWindow.xaml
  /// </summary>
  public partial class MainWindow : Window
  {
    public MainWindow()
    {
      InitializeComponent();
      DataContext = new GaugeViewModel();
      
      Canvas canvas = new Canvas();

      var g = new StreamGeometry();
      var g1 = new StreamGeometry();

      using (var gc = g.Open())
      {
        gc.BeginFigure(
            startPoint: new Point(90, 275),
            isFilled: false,
            isClosed: false);

        gc.ArcTo(
            point: new Point(210, 275),
            size: new Size(100, 100),
            rotationAngle: 0d,
            isLargeArc: true,
            sweepDirection: SweepDirection.Clockwise,
            isStroked: true,
            isSmoothJoin: false);
      }

      var path = new Path
      {
        Stroke = Brushes.Cyan,
        StrokeThickness = 5,
        Data = g
      };
      canvas.Children.Add(path);
      using (var gc = g1.Open())
      {
        gc.BeginFigure(
            startPoint: new Point(90, 275),
            isFilled: false,
            isClosed: false);

        gc.ArcTo(
            point: new Point(210, 20),
            size: new Size(100, 100),
            rotationAngle: 0d,
            isLargeArc: true,
            sweepDirection: SweepDirection.Clockwise,
            isStroked: true,
            isSmoothJoin: false);
      }

      var path1 = new Path
      {
        Stroke = Brushes.Red,
        StrokeThickness = 5,
        Data = g1
      };
      canvas.Children.Add(path1);
      canBackArea.Children.Add(canvas);
    }
  }


}
