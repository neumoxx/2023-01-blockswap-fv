pragma solidity 0.8.13;

// SPDX-License-Identifier: MIT

import { Initializable } from "@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol";
import { ContextUpgradeable } from "@openzeppelin/contracts-upgradeable/utils/ContextUpgradeable.sol";
import { IERC20Upgradeable } from "@openzeppelin/contracts-upgradeable/token/ERC20/IERC20Upgradeable.sol";
import { IERC20MetadataUpgradeable } from "@openzeppelin/contracts-upgradeable/token/ERC20/extensions/IERC20MetadataUpgradeable.sol";
import { ISlotSettlementRegistry } from "../munged/interfaces/ISlotSettlementRegistry.sol";
import { ScaledMath } from "../munged/libraries/ScaledMath.sol";

contract  MocksETH is  Initializable, ContextUpgradeable, IERC20Upgradeable, IERC20MetadataUpgradeable {
    using ScaledMath for uint256;

    /// @notice Address of registry of all SLOT tokens
    ISlotSettlementRegistry public slotRegistry;
    uint256 public constant BASE_EXCHANGE_RATE = 3 ether;
    
    mapping(address => uint256) private _balances;

    mapping(address => mapping(address => uint256)) private _allowances;

    uint256 private _totalSupply;

    string private _name;
    string private _symbol;

    /// @custom:oz-upgrades-unsafe-allow constructor
    constructor() initializer {}
    
    function name() public view virtual override returns (string memory) {
        return _name;
    }
    
    function symbol() public view virtual override returns (string memory) {
        return _symbol;
    }
    
    function decimals() public view virtual override returns (uint8) {
        return 18;
    }
    
    function totalSupply() public view virtual override returns (uint256) {
        return _totalSupply;
    }
    
    function balanceOf(address account) public view virtual override returns (uint256) {
        return _balances[account];
    }
    
    function transfer(address to, uint256 amount) public virtual override returns (bool) {
        address owner = _msgSender();
        uint256 fromBalance = _balances[owner];
        if(fromBalance < amount) return false;
        _transfer(owner, to, amount);
        return true;
    }
    
    function allowance(address owner, address spender) public view virtual override returns (uint256) {
        return _allowances[owner][spender];
    }
    
    function approve(address spender, uint256 amount) public virtual override returns (bool) {
        address owner = _msgSender();
        _approve(owner, spender, amount);
        return true;
    }
    
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public virtual override returns (bool) {
        address spender = _msgSender();
        if(_balances[from] < amount || _allowances[from][spender] < amount) return false;
        _spendAllowance(from, spender, amount);
        _transfer(from, to, amount);
        return true;
    }
    
    function increaseAllowance(address spender, uint256 addedValue) public virtual returns (bool) {
        address owner = _msgSender();
        _approve(owner, spender, allowance(owner, spender) + addedValue);
        return true;
    }
    
    function decreaseAllowance(address spender, uint256 subtractedValue) public virtual returns (bool) {
        address owner = _msgSender();
        uint256 currentAllowance = allowance(owner, spender);
        require(currentAllowance >= subtractedValue, "ERC20: decreased allowance below zero");
        unchecked {
            _approve(owner, spender, currentAllowance - subtractedValue);
        }

        return true;
    }
    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual {
        require(from != address(0), "ERC20: transfer from the zero address");
        require(to != address(0), "ERC20: transfer to the zero address");

        _beforeTokenTransfer(from, to, amount);

        uint256 fromBalance = _balances[from];
        require(fromBalance >= amount, "ERC20: transfer amount exceeds balance");
        unchecked {
            _balances[from] = fromBalance - amount;
            // Overflow not possible: the sum of all balances is capped by totalSupply, and the sum is preserved by
            // decrementing then incrementing.
            _balances[to] += amount;
        }

        emit Transfer(from, to, amount);

        _afterTokenTransfer(from, to, amount);
    }
    
    function _mint(address account, uint256 amount) internal virtual {
        require(account != address(0), "ERC20: mint to the zero address");

        _beforeTokenTransfer(address(0), account, amount);

        _totalSupply += amount;
        unchecked {
            // Overflow not possible: balance + amount is at most totalSupply + amount, which is checked above.
            _balances[account] += amount;
        }
        emit Transfer(address(0), account, amount);

        _afterTokenTransfer(address(0), account, amount);
    }
    
    function _burn(address account, uint256 amount) internal virtual {
        require(account != address(0), "ERC20: burn from the zero address");

        _beforeTokenTransfer(account, address(0), amount);

        uint256 accountBalance = _balances[account];
        require(accountBalance >= amount, "ERC20: burn amount exceeds balance");
        unchecked {
            _balances[account] = accountBalance - amount;
            // Overflow not possible: amount <= accountBalance <= totalSupply.
            _totalSupply -= amount;
        }

        emit Transfer(account, address(0), amount);

        _afterTokenTransfer(account, address(0), amount);
    }
    
    function _approve(
        address owner,
        address spender,
        uint256 amount
    ) internal virtual {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
    
    function _spendAllowance(
        address owner,
        address spender,
        uint256 amount
    ) internal virtual {
        uint256 currentAllowance = allowance(owner, spender);
        if (currentAllowance != type(uint256).max) {
            require(currentAllowance >= amount, "ERC20: insufficient allowance");
            unchecked {
                _approve(owner, spender, currentAllowance - amount);
            }
        }
    }
    
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual {}
    
    function _afterTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual {}

    /// @notice Used in place of a constructor to support proxies
    /// @dev Can only be called once
    function init() external initializer {
        slotRegistry = ISlotSettlementRegistry(msg.sender);
    }

    /// @notice Mints a given amount of tokens
    /// @dev Only slot settlement registry module can call
    /// @param _recipient of the tokens
    /// @param _amount of tokens to mint
    function mint(address _recipient, uint256 _amount) external {
        require(msg.sender == address(slotRegistry), "mint: Only SLOT registry");
        _mint(_recipient, _amount);
    }

    /// @notice Burns a given amount of tokens
    /// @dev Only slot settlement registry module can call
    /// @param _owner of the tokens
    /// @param _amount of tokens to burn
    function burn(address _owner, uint256 _amount) external {
        require(msg.sender == address(slotRegistry), "burn: Only SLOT registry");
        _burn(_owner, _amount);
    }

    /// @notice Get the address of the associated Stakehouse registry
    function stakehouse() public view returns (address) {
        return slotRegistry.shareTokensToStakeHouse(
            address(this)
        );
    }

    /// @notice Total collateralised SLOT associated with Stakehouse
    function stakehouseCollateralisedSlot() public view returns (uint256) {
        return slotRegistry.circulatingCollateralisedSlot(stakehouse());
    }

    /// @notice For an account with sETH, the amount of SLOT backing those tokens based on actual balance
    /// @param _owner Account containing sETH tokens
    function slot(address _owner) external view returns (uint256) {
        if (_owner == address(slotRegistry)) {
            return stakehouseCollateralisedSlot();
        }

        return slotRegistry.slotForSETHBalance(stakehouse(), balanceOf(_owner));
    }

    /// @notice For an account with sETH, the amount of SLOT backing those tokens based on active balance
    /// @param _owner Account containing sETH tokens
    function slotForActiveBalance(address _owner) external view returns (uint256) {
        if (_owner == address(slotRegistry)) {
            return stakehouseCollateralisedSlot();
        }

        return balanceOf(_owner).sDivision(BASE_EXCHANGE_RATE);
    }

    /// @notice sETH balance of owner factoring in the latest exchange rate of the Stakehouse
    /// @param _owner Account containing sETH tokens
    function activeBalanceOf(address _owner) public view returns (uint256) {
        uint256 sETHBalance = slotRegistry.sETHForSLOTBalance(stakehouse(), balanceOf(_owner));
        return sETHBalance.sDivision(BASE_EXCHANGE_RATE);
    }

    uint256[45] private __gap;
}
