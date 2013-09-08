from qgis.core import QgsSymbolLayerV2Utils

def color_part(partname, values, feature, parent):
    try:
        function = functions[partname]
    except KeyError:
        parent.setEvalErrorString("Color part {0} not found".format(partname))
        return None
    
    function(values, feature, parent)

def red(values, feature, parent):
    """
        Returns the red component of a color
        
        <p><h4>Syntax</h4>
        red(<i>color</i>)</p>

        <p><h4>Arguments</h4>
        <i>  color</i> &rarr; a color<br></p>
        
        <p><h4>Example</h4>
        <!-- Show example of function.-->
             red('255,0,0') &rarr; 255</p>
    """  
    try:
      return QgsSymbolLayerV2Utils.decodeColor(values[0]).red()
    except:
      return None
 
def green(values, feature, parent):
    """
        Returns the green component of a color
        
        <p><h4>Syntax</h4>
        green(<i>color</i>)</p>

        <p><h4>Arguments</h4>
        <i>  color</i> &rarr; a color<br></p>
        
        <p><h4>Example</h4>
        <!-- Show example of function.-->
             green('0,255,0') &rarr; 255</p>
    """  
    try:
      return QgsSymbolLayerV2Utils.decodeColor(values[0]).green()
    except:
      return None      

def blue(values, feature, parent):
    """
        Returns the blue component of a color
        
        <p><h4>Syntax</h4>
        blue(<i>color</i>)</p>

        <p><h4>Arguments</h4>
        <i>  color</i> &rarr; a color<br></p>
        
        <p><h4>Example</h4>
        <!-- Show example of function.-->
             blue('0,0,255') &rarr; 255</p>
    """  
    try:
      return QgsSymbolLayerV2Utils.decodeColor(values[0]).blue()
    except:
      return None
      
def alpha(values, feature, parent):
    """
        Returns the alpha component of a color
        
        <p><h4>Syntax</h4>
        alpha(<i>color</i>)</p>

        <p><h4>Arguments</h4>
        <i>  color</i> &rarr; a color<br></p>
        
        <p><h4>Example</h4>
        <!-- Show example of function.-->
             alpha('255,255,255,125') &rarr; 125</p>
    """  
    try:
      return QgsSymbolLayerV2Utils.decodeColor(values[0]).alpha()
    except:
      return None
  

def hue(values, feature, parent):
    """
        Returns the hue component of a color, an integer between 0-360
        
        <p><h4>Syntax</h4>
        hue(<i>color</i>)</p>

        <p><h4>Arguments</h4>
        <i>  color</i> &rarr; a color<br></p>
        
        <p><h4>Example</h4>
        <!-- Show example of function.-->
             hue('255,0,0') &rarr; 0</p>
    """  
    try:
      # Hue ranges from 0 - 360
      return int(QgsSymbolLayerV2Utils.decodeColor(values[0]).hueF() * 360)
    except:
      return None                 

def saturation(values, feature, parent):
    """
        Returns the saturation of a color, an integer between 0-100
        
        <p><h4>Syntax</h4>
        saturation(<i>color</i>)</p>

        <p><h4>Arguments</h4>
        <i>  color</i> &rarr; a color<br></p>
        
        <p><h4>Example</h4>
        <!-- Show example of function.-->
             saturation('125,255,125') &rarr; 50</p>
    """  
    try:
      # Saturation ranges from 0 - 100
      return int(QgsSymbolLayerV2Utils.decodeColor(values[0]).saturationF() * 100)
    except:
      return None

def lightness(values, feature, parent):
    """
        Returns the lightness of a color, an integer between 0-100
        
        <p><h4>Syntax</h4>
        lightness(<i>color</i>)</p>

        <p><h4>Arguments</h4>
        <i>  color</i> &rarr; a color<br></p>
        
        <p><h4>Example</h4>
        <!-- Show example of function.-->
             lightness('125,255,125') &rarr; 74</p>
    """  
    try:
      # Lightness ranges from 0 - 100
      return int(QgsSymbolLayerV2Utils.decodeColor(values[0]).lightnessF() * 100)
    except:
      return None

def hsv_value(values, feature, parent):
    """
        Returns the hsv value component of a color, an integer between 0-100
        
        <p><h4>Syntax</h4>
        hsv_value(<i>color</i>)</p>

        <p><h4>Arguments</h4>
        <i>  color</i> &rarr; a color<br></p>
        
        <p><h4>Example</h4>
        <!-- Show example of function.-->
             hsv_value('125,255,125') &rarr; 100</p>
    """  
    try:
      # Value ranges from 0 - 100
      return int(QgsSymbolLayerV2Utils.decodeColor(values[0]).valueF() * 100)
    except:
      return None

def set_red(values, feature, parent):
    """
        Sets the red component of a color
        
        <p><h4>Syntax</h4>
        set_red(<i>color</i>, <i>red</i>)</p>

        <p><h4>Arguments</h4>
        <i>  color</i> &rarr; a color<br>
        <i>  red</i> &rarr; a integer between 0 and 255<br></p>
        
        <p><h4>Example</h4>
        <!-- Show example of function.-->
             set_red('255,255,255', 125) &rarr; '125,255,255'</p>
    """  
    try:
      color = QgsSymbolLayerV2Utils.decodeColor(values[0])
      color.setRed(values[1])
      return QgsSymbolLayerV2Utils.encodeColor(color)
    except: 
      return None

def set_green(values, feature, parent):
    """
        Sets the blue component of a color
        
        <p><h4>Syntax</h4>
        set_green(<i>color</i>, <i>blue</i>)</p>

        <p><h4>Arguments</h4>
        <i>  color</i> &rarr; a color<br>
        <i>  green</i> &rarr; a integer between 0 and 255<br></p>
        
        <p><h4>Example</h4>
        <!-- Show example of function.-->
             set_green('255,255,255', 125) &rarr; '255,125,255'</p>
    """  
    try:
      color = QgsSymbolLayerV2Utils.decodeColor(values[0])
      color.setGreen(values[1])
      return QgsSymbolLayerV2Utils.encodeColor(color)
    except: 
      return None  
      
def set_blue(values, feature, parent):
    """
        Sets the blue component of a color
        
        <p><h4>Syntax</h4>
        set_blue(<i>color</i>, <i>blue</i>)</p>

        <p><h4>Arguments</h4>
        <i>  color</i> &rarr; a color<br>
        <i>  blue</i> &rarr; a integer between 0 and 255<br></p>
        
        <p><h4>Example</h4>
        <!-- Show example of function.-->
             set_blue('255,255,255', 125) &rarr; '255,255,125'</p>
    """  
    try:
      color = QgsSymbolLayerV2Utils.decodeColor(values[0])
      color.setBlue(values[1])
      return QgsSymbolLayerV2Utils.encodeColor(color)
    except: 
      return None

def set_hue(values, feature, parent):
    """
        Sets the hue component of a color
        
        <p><h4>Syntax</h4>
        set_hue(<i>color</i>, <i>hue</i>)</p>

        <p><h4>Arguments</h4>
        <i>  color</i> &rarr; a color<br>
        <i>  hue</i> &rarr; a integer between 0 and 360<br></p>
        
        <p><h4>Example</h4>
        <!-- Show example of function.-->
             set_hue('0,255,0,255', 0) &rarr; '255,0,0,255'</p>
    """  
    try:
      color = QgsSymbolLayerV2Utils.decodeColor(values[0])
      color.setHslF(values[1] / 360.0, color.saturationF(), color.lightnessF(), color.alphaF())
      return QgsSymbolLayerV2Utils.encodeColor(color)
    except: 
      return None
      
def set_saturation(values, feature, parent):
    """
        Sets the saturation of a color
        
        <p><h4>Syntax</h4>
        set_saturation(<i>color</i>, <i>saturation</i>)</p>

        <p><h4>Arguments</h4>
        <i>  color</i> &rarr; a color<br>
        <i>  saturation</i> &rarr; a integer between 0 and 100<br></p>
        
        <p><h4>Example</h4>
        <!-- Show example of function.-->
             set_saturation('0,255,0,255', 0) &rarr; '128,128,128,125'</p>
    """  
    try:
      color = QgsSymbolLayerV2Utils.decodeColor(values[0])
      color.setHslF(color.hueF(), values[1] / 100.0, color.lightnessF(), color.alphaF())
      return QgsSymbolLayerV2Utils.encodeColor(color)
    except: 
      return None
      

def set_lightness(values, feature, parent):
    """
        Sets the lightness of a color
        
        <p><h4>Syntax</h4>
        set_lightness(<i>color</i>, <i>lightness</i>)</p>

        <p><h4>Arguments</h4>
        <i>  color</i> &rarr; a color<br>
        <i>  lightness</i> &rarr; a integer between 0 and 100<br></p>
        
        <p><h4>Example</h4>
        <!-- Show example of function.-->
             set_lightness('0,255,0,255', 10) &rarr; '0,51,0,255'</p>
    """  
    try:
      color = QgsSymbolLayerV2Utils.decodeColor(values[0])
      color.setHslF(color.hueF(), color.saturationF(), values[1] / 100.0, color.alphaF())
      return QgsSymbolLayerV2Utils.encodeColor(color)
    except: 
      return None

def set_hsv_value(values, feature, parent):
    """
        Sets the value of a color
        
        <p><h4>Syntax</h4>
        set_hsv_value(<i>color</i>, <i>value</i>)</p>

        <p><h4>Arguments</h4>
        <i>  color</i> &rarr; a color<br>
        <i>  value</i> &rarr; a integer between 0 and 100<br></p>
        
        <p><h4>Example</h4>
        <!-- Show example of function.-->
             set_hsv_value('0,255,0,255', 50) &rarr; '0,128,0,255'</p>
    """  
    try:
      color = QgsSymbolLayerV2Utils.decodeColor(values[0])
      color.setHsvF(color.hueF(), color.saturationF(), values[1] / 100.0, color.alphaF())
      return QgsSymbolLayerV2Utils.encodeColor(color)
    except: 
      return None                                    

def set_alpha(values, feature, parent):
    """
        Sets the alpha component of a color
        
        <p><h4>Syntax</h4>
        set_alpha(<i>color</i>, <i>alpha</i>)</p>

        <p><h4>Arguments</h4>
        <i>  color</i> &rarr; a color<br>
        <i>  alpha</i> &rarr; an alpha value between 0 and 255<br></p>
        
        <p><h4>Example</h4>
        <!-- Show example of function.-->
             set_alpha('255,255,255,255', 125) &rarr; '255,255,255,125'</p>
    """  
    try:
      color = QgsSymbolLayerV2Utils.decodeColor(values[0])
      color.setAlpha(values[1])
      return QgsSymbolLayerV2Utils.encodeColor(color)
    except: 
      return None   
  

functions = {"get_red": red,
             "get_green": green,
             "get_blue": blue,
             "get_aplha": alpha,
             "get_hsv": hsv_value,
             "get_saturation": saturation,
             "get_lightness": lightness,
             "set_red": set_red,
             "set_green": set_green,
             "set_blue": set_blue,
             "set_aplha": set_alpha,
             "set_hsv": set_hsv_value,
             "set_saturation": set_saturation,
             "set_lightness": set_lightness
             }