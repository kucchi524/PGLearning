package learning4;

public class Item {
	
	String name;
	
	int price;
	
	int quantity;
	
	public Item(String name, int quantity, int price) {
		this.name = name;
		this.quantity = quantity;
		this.price = price;
	}
	
	public int getSubtotal() {
		
		return price * quantity;
	}
	
	public String getInfo() {
		return "商品名: " + name + " / 単価; " + price + "円 / 数量: " + quantity + " / 小計: " + getSubtotal();
	}

}
