// = commented code
//__ = Explanation and/or idea

class Main {//-----------
    public static void main(String[] args) {//**********
      
      //Item item = new Item ("Xbox Controller");
      //Item item2 = new Item ("HDMI Cable");
  
    //item.details("Compatible with Xbox one, X|S series, and PC");
  
      Item usbCable = new Item(10.75, "USB type-c", "USB Cable");
      Item cable = new Item(10.75, "HDMI 3x", "HDMI Cable");
      Item controller = new Item(34.75, "Xbox Controller", "game pad");
      Item tv = new Item(150, "LG Television", "TV");
      //System.out.println(item.getName());
      //System.out.println(usbCable.getName());
      
      Cart useCart = new Cart();
      Customer luis = new Customer("Luis", useCart);
  
      //####### adding to the cart #######
      luis.add_to_cart(usbCable, useCart);
      luis.add_to_cart(cable, useCart);
      luis.add_to_cart(controller, useCart);
      luis.add_to_cart(tv, useCart);
  
      //luis.typeCardinfo();
      System.out.println(useCart.calc_total());
      //luis.addMoneyToCart(400);
      System.out.println(useCart.getTotalPrice());
      System.out.println(luis.getCardBalance());
      luis.check_out(useCart);  //to Chek out items use method object.methodName(Cart parameter)
      /*
      luis.address("1403 Grand Concourse", "Bronx", "NY", "10452");
      System.out.println(luis.get_address());*/
  
      //###### getting the total price ######
      //System.out.println(useCart.calc_total());
      //System.out.println(useCart.getTotalPrice()); -> used for test the total_price
      
      //luis.display_items(useCart);
      //luis.clear_cart(useCart);
  
      /*
      System.out.println(usbCable.get_price());
      usbCable.add_quantity(5);
      System.out.println(usbCable.get_price());
      usbCable.update_quantity();
      luis.display_items(useCart); -> Using again for test */
    }//***********
  }//--------------